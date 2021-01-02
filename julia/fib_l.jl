#!/usr/bin/env julia

print((s->s(s))(s->n->
        if n == 0 || n == 1;
            return 1;
        else
            return s(s)(n - 1) + s(s)(n - 2);
        end)(33),  '\n')

