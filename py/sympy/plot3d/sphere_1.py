#!/usr/bin/env python3
from sympy import *

u, v = symbols('u v')

tref_x = sin(u) * cos(v)
tref_y = sin(u) * sin(v)
tref_z = cos(u)

plotting.plot3d_parametric_surface (tref_x, tref_y, tref_z, (u,0,2*pi), (v,0,2*pi), nb_of_points_u=30, nb_of_points_v=30)

