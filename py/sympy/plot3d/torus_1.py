#!/usr/bin/env python3
# c/o https://www.youtube.com/watch?v=345SnWfahhY 
from sympy import *

u, v = symbols('u v')

tref_x = 3 * cos(u) + cos(u) * cos(v)
tref_y = 3 * sin(u) + sin(u) * cos(v)
tref_z = sin(v)

plotting.plot3d_parametric_surface (tref_x, tref_y, tref_z, (u,0,2*pi), (v,0,2*pi), nb_of_points_u=30, nb_of_points_v=30)

