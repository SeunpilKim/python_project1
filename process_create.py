#!C:\Users\tjsvl\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

with open('data/'+title, 'w') as f:
    f.write(description)

#ReDirection
print("Location: index.py?id=" + title)
print()
