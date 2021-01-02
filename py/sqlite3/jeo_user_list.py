#!/usr/bin/env python3
import sqlite3

c = sqlite3.connect('jeo.db')
cs = c.cursor();

cs.execute ('select * from users')

for u in cs.fetchall():
    print(u)

cs.close()
c.close();

