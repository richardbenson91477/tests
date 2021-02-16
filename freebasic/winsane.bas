#include "SDL2/SDL.bi"
SDL_Init(SDL_INIT_VIDEO)

var tau = 6.283185307
var steps = 100
var circs = 1

var circs_over_steps = circs / steps
var my_tau = circs_over_steps * (tau + (1 / circs))

dim wins(1 to steps) as SDL_Window ptr

for n as integer = 1 to steps
    var t = n * my_tau 
    var x = 500 + (cos(t) * 300.0)
    var y = 500 + (sin(t) * 300.0)
    wins(n) = SDL_CreateWindow("title", x, y, 32, 32, 0)
    sleep 100
    if n > 20 then
        SDL_DestroyWindow(wins(n - 20))
    end if
next n

SDL_Quit()

