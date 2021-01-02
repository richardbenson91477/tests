#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_opengl.h>

    const char *win_name = "sdl_opengl_cube";
    int win_w = 480, win_h = 480;

    int run_t_prev;
    long frames = 0;

    SDL_Window *_window;

    const float n = -1.0f;
    const float p = 1.0f;
    const float box_v[] =
        {p,p,n, n,p,n, n,p,p, p,p,p, p,p,n, n,p,p,
         p,n,p, n,n,p, n,n,n, p,n,n, p,n,p, n,n,n,
         p,p,p, n,p,p, n,n,p, p,n,p, p,p,p, n,n,p,
         p,n,n, n,n,n, n,p,n, p,p,n, p,n,n, n,p,n,
         n,p,p, n,p,n, n,n,n, n,n,p, n,p,p, n,n,n,
         p,p,n, p,p,p, p,n,p, p,n,n, p,p,n, p,n,p};
    float box_rot_t = 0.0f;
 
void report_fps () {
    printf ("%f:", 1000.0 * (float)frames /
            (float)(SDL_GetTicks () - run_t_prev));
    run_t_prev = SDL_GetTicks ();
    frames = 0;
    fflush (stdout);
}

void tick () {
    frames ++;
    if (frames > 5000)
        report_fps ();
    box_rot_t += 0.2f;
    if (box_rot_t > 360.0f)
        box_rot_t -= 360.0f;
}

void paint () {
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode (GL_MODELVIEW);
    glLoadIdentity ();
    glTranslatef (0.0f, 0.0f, -5.0f);
    glRotatef (box_rot_t, -0.5f, 1.0f, -0.5f);
    glDrawArrays (GL_TRIANGLES, 0, 36);

    SDL_GL_SwapWindow (_window);
}

void reshape (int w, int h) {
    win_w = w;
    win_h = h;

    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    float left = -1.0f, bottom = -1.0f;
    glFrustum (left, -left, bottom, -bottom, 2.0f, 50.0f);
    glMatrixMode (GL_MODELVIEW);

    glViewport (0, 0, win_w, win_h);
}

int init () {
    if (SDL_Init (SDL_INIT_VIDEO))
        return -1;

    SDL_GL_SetAttribute (SDL_GL_DOUBLEBUFFER, 1);
    SDL_GL_SetAttribute (SDL_GL_DEPTH_SIZE, 16);

    _window = SDL_CreateWindow (win_name,
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        win_w, win_h,
        SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE);
    if (! _window) 
        return -2;

    if (! SDL_GL_CreateContext (_window))
        return -3;

    SDL_GL_SetSwapInterval (0);

    glEnable (GL_DEPTH_TEST);
    glEnable (GL_CULL_FACE);
    glClearColor (0.0, 0.0, 0.0, 1.0);
    glEnableClientState (GL_VERTEX_ARRAY);
    glEnableClientState (GL_COLOR_ARRAY);
    glVertexPointer (3, GL_FLOAT, 0, box_v);
    glColorPointer (3, GL_FLOAT, 0, box_v);

    reshape (win_w, win_h);

    run_t_prev = SDL_GetTicks ();
    return 0;
}

void deinit () {
    report_fps ();
    printf ("\n");

    SDL_DestroyWindow (_window);
    SDL_Quit ();
}

int main () {
    int res = init ();
    if (res)
        return res;

    SDL_Event event;
    uint8_t done_ = 0;
    while (! done_) {
        while (SDL_PollEvent (&event)) {
            if (event.type == SDL_QUIT) {
                done_ = 1;
                break;
            }
            else if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym == SDLK_ESCAPE) {
                    done_ = 1;
                    break;
                }
            }
            else if (event.type == SDL_WINDOWEVENT) {
                if (event.window.event == SDL_WINDOWEVENT_RESIZED)
                    reshape (event.window.data1, event.window.data2);
            }
        }
        
        if (done_)
            break;

        tick ();
        paint ();
    }

    deinit ();
    return 0;
}

