#!/usr/bin/env python3

import sys, math, os, random, ctypes
import sdl2, sdl2.sdlmixer, sdl2.sdlimage

class s:
    ''' global state '''
    win_s = 'pysdl2'
    win_w, win_h = (640, 480)
    win_bgcolor = 0xff600030
    # win_rect_ref

    run_fps = 25
    # run_t_end, run_t_begin
    # run_frame_t, run_frame_t_ms

    # window, windowsurface
    # mouse_rect

    STATE_PAUSE, STATE_BEGIN, STATE_IDLE, STATE_END, STATE_OVER =\
        range(5)

    # state
    # state_t, state_len, state_next

    N_LAYOUTS = 1
    LAY_LOGO = 0
    layout = [[] for c in range(N_LAYOUTS)]

    IMG_LOGO, IMG_MOUSE =\
        range(2)
    imgs_fns = ['logo', 'mouse']
    # imgs

    SND_BUZZ = 0
    snds_fns = ['buzz']
    # snds

def main ():
    spawn_interact ()

    res = init ()
    if res:
        return res

    event = sdl2.SDL_Event ()
    event_ref = ctypes.byref (event)

    done_ = False
    while not done_:
        while sdl2.SDL_PollEvent (event_ref) != 0:
            if event.type == sdl2.SDL_QUIT:
                done_ = True
                break
            elif event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.keycode.SDLK_ESCAPE:
                    done_ = True
                    break
            elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                if event.button.button is 1:
                    on_click (event.button.x, event.button.y)
            elif event.type == sdl2.SDL_MOUSEMOTION:
                on_move (event.motion.x, event.motion.y)
        if done_:
            break
        tick ()
        paint ()

    deinit ()
    return 0

def init ():
    if sdl2.SDL_Init (sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_AUDIO):
        return -1

    s.window = sdl2.SDL_CreateWindow (bytes(s.win_s.encode ()),
        sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
        s.win_w, s.win_h,
        sdl2.SDL_WINDOW_SHOWN)
    if not s.window:
        return -2

    s.windowsurface = sdl2.SDL_GetWindowSurface (s.window)

    sdl2.mouse.SDL_ShowCursor (False)

    random.seed ()

    s.win_rect_ref = ctypes.byref (sdl2.SDL_Rect (0, 0, s.win_w, s.win_h))

    s.imgs = [sdl2.sdlimage.IMG_Load (
        bytes (os.path.join ('data', fn + '.png').encode ()))
        for fn in s.imgs_fns]

    s.mouse_rect = sdl2.SDL_Rect (0, 0,
        s.imgs[s.IMG_MOUSE].contents.w, s.imgs[s.IMG_MOUSE].contents.h)

    sdl2.sdlmixer.Mix_OpenAudio (
        sdl2.sdlmixer.MIX_DEFAULT_FREQUENCY,
        sdl2.sdlmixer.MIX_DEFAULT_FORMAT,
        sdl2.sdlmixer.MIX_DEFAULT_CHANNELS,
        4096)
    sdl2.sdlmixer.Mix_Init (sdl2.sdlmixer.MIX_INIT_OGG)

    s.snds = [sdl2.sdlmixer.Mix_LoadWAV (
        bytes (os.path.join ('data', fn + '.ogg').encode()))
        for fn in s.snds_fns]

    s.state = s.STATE_PAUSE
    s.state_next = s.STATE_PAUSE
    s.state_t = 0.0
    s.state_len = 0.0

    init_layout ()
    init_game ()

    s.run_frame_t = 1.0 / s.run_fps
    s.run_frame_t_ms = int(s.run_frame_t * 1000.0)
    s.run_t_begin = s.run_t_end = sdl2.SDL_GetTicks ()
    return 0

def deinit ():
    sdl2.sdlmixer.Mix_Quit ()
    sdl2.SDL_DestroyWindow (s.window)
    sdl2.SDL_Quit ()

def tick ():
    s.run_t_end = sdl2.SDL_GetTicks ()
    _t = s.run_t_begin - s.run_t_end + s.run_frame_t_ms
    if _t > 0:
        sdl2.SDL_Delay (_t)
    s.run_t_begin = sdl2.SDL_GetTicks ()

    if s.state_len > 0.0:
        s.state_t += s.run_frame_t
        if s.state_t >= s.state_len:
            s.state_t = 0.0
            set_state ()

    if s.state == s.STATE_BEGIN:
        return
    elif s.state == s.STATE_IDLE:
        return
    elif s.state == s.STATE_END:
        return
    elif s.state == s.STATE_OVER:
        return

def paint ():
    sdl2.SDL_FillRect (s.windowsurface, s.win_rect_ref, s.win_bgcolor)

    sdl2.SDL_BlitSurface (s.imgs[s.IMG_LOGO], None, s.windowsurface,
        s.layout[s.LAY_LOGO])

    sdl2.SDL_BlitSurface (s.imgs[s.IMG_MOUSE], None, s.windowsurface,
        s.mouse_rect)

    sdl2.SDL_UpdateWindowSurface (s.window)

def on_click (mx, my):
    s.mouse_rect.x = mx
    s.mouse_rect.y = my
    sdl2.sdlmixer.Mix_PlayChannel (0, s.snds[s.SND_BUZZ], 0)

def on_move (mx, my):
    s.mouse_rect.x = mx
    s.mouse_rect.y = my

def init_layout ():
    win_hw, win_hh = (s.win_w // 2, s.win_h // 2)
    logo_hw = s.imgs[s.IMG_LOGO].contents.w // 2
    logo_hh = s.imgs[s.IMG_LOGO].contents.h // 2

    x = win_hw - logo_hw
    y = win_hh - logo_hh
    s.layout[s.LAY_LOGO] = sdl2.SDL_Rect (x, y)

def p_in_r (x, y, r):
    if x >= r.x and y >= r.y and x < r.x + r.w and y < r.y + r.h:
        return True
    return False

def init_game ():
    set_state (s.STATE_BEGIN)

def set_state (state = False):
    if state:
        s.state = state
    else:
        s.state = s.state_next

    if s.state == s.STATE_BEGIN:
        s.state_next = s.STATE_IDLE
        s.state_len = 1.0
        return

    elif s.state == s.STATE_END:
        s.state = s.state_next = s.STATE_OVER
        s.state_len = 0.0
        return

locs = locals ()
def spawn_interact ():
    import threading
    def t_fun ():
        import code
        code.interact (local = locs)
    threading.Thread (target = t_fun).start ()

if __name__ == '__main__':
    sys.exit (main ())

