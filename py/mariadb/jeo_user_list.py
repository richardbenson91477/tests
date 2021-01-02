#!/usr/bin/env python3

import pymysql.cursors

c = pymysql.connect('localhost', 'rich', '50915', cursorclass=pymysql.cursors.DictCursor)
cs = c.cursor();
cs.execute ('use jeo')
cs.execute ('select * from users');
u = cs.fetchall()
for i in u:
    print(i['name'], i['uuid'])

cs.close();
c.close();

