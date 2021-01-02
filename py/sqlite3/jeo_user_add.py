#!/usr/bin/env python3
import uuid
import sqlite3

name = input('name: ')
uuid = uuid.uuid1().hex;
print(f"Generated uuid \"{uuid}\" for user \"{name}\"")

c = sqlite3.connect('jeo.db')
cs = c.cursor();

sql = f"insert into users (uuid, name) values (\'{uuid}\', \'{name}\');"
#print(sql)
cs.execute (sql)

u = cs.fetchall()
print(u)

c.commit()

cs.close()
c.close();

