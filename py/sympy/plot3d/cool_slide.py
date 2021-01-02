#!/usr/bin/env python3
from sympy import *

u, v = symbols('u v')

tref_x = sin(u*3) + cos(u/2) + 0.01*v
tref_y = cos(u*3) + sin(u/2) + 0.01*v
tref_z = u/pi + 0.01*v

plotting.plot3d_parametric_surface (tref_x, tref_y, tref_z, (u,0,4*pi), (v,0,2*pi), nb_of_points_u=50, nb_of_points_v=5)
