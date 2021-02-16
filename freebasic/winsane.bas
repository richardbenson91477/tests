#include "SDL2/SDL.bi"
SDL_Init(SDL_INIT_VIDEO)

for n as integer = 1 to 100
    var t = (n / 100) * 6.283185307
    var x = 300 + (cos(t) * 300.0)
    var y = 300 + (sin(t) * 300.0)
    var win = SDL_CreateWindow("title", x, y, 32, 32, 0)
next n

sleep 1000

SDL_Quit()
