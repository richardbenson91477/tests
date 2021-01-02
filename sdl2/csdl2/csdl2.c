#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <limits.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_mixer.h>
#include <SDL2/SDL_image.h>

    const char *win_name = "csdl2";
    int32_t win_w = 640;
    int32_t win_h = 480;
    uint32_t win_bgcolor = 0xff600030;
    SDL_Rect win_rect;

    float run_fps = 25;
    float run_frame_t;
    uint32_t run_t_begin, run_t_end, run_frame_t_ms;

    SDL_Window *window;
    SDL_Surface *windowsurface;
    SDL_Rect mouse_rect;

    enum {
        STATE_PAUSE = 1, STATE_BEGIN, STATE_IDLE, STATE_END, STATE_OVER
    };
    uint32_t state, state_next;
    float state_t, state_len;

    #define LAYOUT_N (1)
    enum {
        LAY_LOGO
    };
    SDL_Rect layout[LAYOUT_N];

    #define IMG_N (2)
    enum {
        IMG_LOGO, IMG_MOUSE
    };
    const char *img_fns[IMG_N] = {"logo", "mouse"};
    SDL_Surface *imgs[IMG_N];

    #define SND_N (1)
    enum {
        SND_BUZZ
    };
    const char *snd_fns[SND_N] = {"buzz"};
    Mix_Chunk *snds[SND_N];

void init ();
void deinit ();
void tick ();
void paint ();
void on_click (int32_t mx, int32_t my);
void on_move (int32_t mx, int32_t my);
void init_layout ();
uint8_t p_in_r (int32_t x, int32_t y, SDL_Rect r);
void init_game ();
void set_state (uint32_t state);

int main () {
    SDL_Event event;
    int32_t done;

    init ();

    done = 0;
    while (! done) {
        while (SDL_PollEvent (&event) != 0) {
            if (event.type == SDL_QUIT) {
                done = 1;
                break;
            }
            else if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym == SDLK_ESCAPE) {
                    done = 1;
                    break;
                }
            }
            else if (event.type == SDL_MOUSEBUTTONDOWN) {
                if (event.button.button == 1)
                    on_click (event.button.x, event.button.y);
            }
            else if (event.type == SDL_MOUSEMOTION)
                on_move (event.motion.x, event.motion.y);
        }
        if (done)
            break;
        tick ();
        paint ();
    }

    deinit ();
    return 0;
}

void init () {
    char fname [PATH_MAX + 1];
    uint32_t c;

    SDL_Init (SDL_INIT_VIDEO | SDL_INIT_AUDIO);

    window = SDL_CreateWindow (win_name,
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        win_w, win_h,
        SDL_WINDOW_SHOWN);
    windowsurface = SDL_GetWindowSurface (window);

    SDL_ShowCursor (0);

    win_rect.x = 0;
    win_rect.y = 0;
    win_rect.w = win_w;
    win_rect.h = win_h;

    for (c = 0; c < IMG_N; c ++) {
        sprintf (fname, "data/%s.png", img_fns[c]);
        imgs[c] = IMG_Load (fname);
    }

    mouse_rect.x = 0;
    mouse_rect.y = 0;
    mouse_rect.w = imgs[IMG_MOUSE]->w;
    mouse_rect.h = imgs[IMG_MOUSE]->h;

    Mix_OpenAudio (MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT,
        MIX_DEFAULT_CHANNELS, 4096);
    Mix_Init (MIX_INIT_OGG);

    for (c = 0; c < SND_N; c ++) {
        sprintf (fname, "data/%s.ogg", snd_fns[c]);
        snds[c] = Mix_LoadWAV (fname);
    }

    state = STATE_PAUSE;
    state_next = STATE_PAUSE;
    state_t = 0.0;
    state_len = 0.0;

    init_layout ();
    init_game ();

    run_frame_t = 1.0 / run_fps;
    run_frame_t_ms = (uint32_t)(run_frame_t * 1000.0);
    run_t_begin = run_t_end = SDL_GetTicks ();
}

void deinit () {
    Mix_Quit ();
    SDL_DestroyWindow (window);
    SDL_Quit ();
}

void tick () {
    int32_t _t;

    run_t_end = SDL_GetTicks ();
    _t = run_t_begin - run_t_end + run_frame_t_ms;
    if (_t > 0)
        SDL_Delay (_t);
    run_t_begin = SDL_GetTicks ();

    if (state_len > 0.0) {
        state_t += run_frame_t;
        if (state_t >= state_len) {
            state_t = 0.0;
            set_state (0);
        }
    }

    if (state == STATE_BEGIN)
        return;
    else if (state == STATE_IDLE)
        return;
    else if (state == STATE_END)
        return;
    else if (state == STATE_OVER)
        return;
}

void paint () {
    SDL_FillRect (windowsurface, &win_rect, win_bgcolor);
    SDL_BlitSurface (imgs[IMG_LOGO], NULL, windowsurface, &layout[LAY_LOGO]);
    SDL_BlitSurface (imgs[IMG_MOUSE], NULL, windowsurface, &mouse_rect);
    SDL_UpdateWindowSurface (window);
}

void on_click (int32_t mx, int32_t my) {
    mouse_rect.x = mx;
    mouse_rect.y = my;
    Mix_PlayChannel (0, snds[SND_BUZZ], 0);
}

void on_move (int32_t mx, int32_t my) {
    mouse_rect.x = mx;
    mouse_rect.y = my;
}

void init_layout () {
    uint32_t win_hw, win_hh;
    uint32_t logo_hw, logo_hh;

    win_hw = win_w / 2;
    win_hh = win_h / 2;
    logo_hw = imgs[IMG_LOGO]->w / 2;
    logo_hh = imgs[IMG_LOGO]->h / 2;
    layout[LAY_LOGO].x = win_hw - logo_hw;
    layout[LAY_LOGO].y = win_hh - logo_hh;
}

uint8_t p_in_r (int32_t x, int32_t y, SDL_Rect r) {
    if ((x >= r.x) && (y >= r.y) && (x < r.x + r.w) && (y < r.y + r.h))
        return 1;
    return 0;
}

void init_game () {
    set_state (STATE_BEGIN);
}

void set_state (uint32_t state) {
    if (state)
        state = state;
    else
        state = state_next;

    if (state == STATE_BEGIN) {
        state_next = STATE_IDLE;
        state_len = 1.0;
    }
    else if (state == STATE_END) {
        state = state_next = STATE_OVER;
        state_len = 0.0;
    }
}

