#!/usr/bin/env python3
import uuid
import pymysql.cursors

name = input('name: ')
uuid = uuid.uuid1().hex;
print(f"Generated uuid \"{uuid}\" for user \"{name}\"")

c = pymysql.connect('localhost', 'rich', '50915', cursorclass=pymysql.cursors.DictCursor)
cs = c.cursor();
cs.execute ('use jeo')

sql = f"insert into users (uuid, name) values (\'{uuid}\', \'{name}\');"
#print(sql)
cs.execute (sql)

u = cs.fetchall()
print(u)

c.commit()

cs.close()
c.close();

