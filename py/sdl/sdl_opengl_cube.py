#!/usr/bin/env python3

import sys, math, os, ctypes
import sdl2
from OpenGL.GL import *

class s:
    ''' global state '''
    win_s = 'sdl_opengl_cube'
    win_w, win_h = (480, 480)
    win_bgcolor = 0xff600030

    run_fps = 60.0
    # run_t_end, run_t_begin
    # run_frame_t, run_frame_t_ms

    # window, context
    
    n = -1.0
    p = 1.0
    box_v = ((p, p, n), (n, p, n), (n, p, p), (p, p, p), (p, p, n), (n, p, p),
        (p, n, p), (n, n, p), (n, n, n), (p, n, n), (p, n, p), (n, n, n),
        (p, p, p), (n, p, p), (n, n, p), (p, n, p), (p, p, p), (n, n, p),
        (p, n, n), (n, n, n), (n, p, n), (p, p, n), (p, n, n), (n, p, n),
        (n, p, p), (n, p, n), (n, n, n), (n, n, p), (n, p, p), (n, n, n),
        (p, p, n), (p, p, p), (p, n, p), (p, n, n), (p, p, n), (p, n, p))
    box_rot_t = 0.0

def main ():
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
            elif event.type == sdl2.SDL_WINDOWEVENT:
                if event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                    reshape (event.window.data1, event.window.data2)
                    break
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
        sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_RESIZABLE)
    if not s.window:
        return -2

    s.context = sdl2.SDL_GL_CreateContext (s.window)
    sdl2.SDL_GL_MakeCurrent (s.window, s.context)

    glEnable (GL_DEPTH_TEST)
    glClearColor (0.0, 0.0, 0.0, 1.0)

    reshape (s.win_w, s.win_h)

    s.run_frame_t = 1.0 / s.run_fps
    s.run_frame_t_ms = int(s.run_frame_t * 1000.0)
    s.run_t_begin = s.run_t_end = sdl2.SDL_GetTicks ()
    return 0

def deinit ():
    sdl2.SDL_GL_DeleteContext (s.context)
    sdl2.SDL_DestroyWindow (s.window)
    sdl2.SDL_Quit ()

def tick ():
    s.run_t_end = sdl2.SDL_GetTicks ()
    _t = s.run_t_begin - s.run_t_end + s.run_frame_t_ms
    if _t > 0:
        sdl2.SDL_Delay (_t)
    s.run_t_begin = sdl2.SDL_GetTicks ()

    s.box_rot_t += 2.0
    if s.box_rot_t > 360.0:
        s.box_rot_t -= 360.0

def paint ():
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()
    glTranslatef (0.0, 0.0, -5.0)
    glRotatef (s.box_rot_t, -0.5, 1.0, -0.5)

    glBegin (GL_TRIANGLES)
    for pv in s.box_v:
        glColor3f (pv[0], pv[1], pv[2])
        glVertex3f (pv[0], pv[1], pv[2])
    glEnd ()

    sdl2.SDL_GL_SwapWindow (s.window)
    pass

def reshape (w, h):
    s.win_w = w
    s.win_h = h

    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    left = -1.0
    right = -left
    bottom = -1.0
    top = -bottom
    glFrustum (left, right, bottom, top, 2, 50)
    glMatrixMode (GL_MODELVIEW)
    
    glViewport (0, 0, w, h)

if __name__ == '__main__':
    sys.exit (main ())

