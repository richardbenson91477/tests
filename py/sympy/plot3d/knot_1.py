#!/usr/bin/env python3
from sympy import *

u, v = symbols('u v')

tref_x = sin(u) + 2*sin(2*u) + 0.1*sin(v)
tref_y = cos(u) - 2*cos(2*u) + 0.1*cos(v)
tref_z = -sin(3*u)

plotting.plot3d_parametric_surface (tref_x, tref_y, tref_z, (u,0,2*pi), (v,0,2*pi), nb_of_points_u=50, nb_of_points_v=4)

