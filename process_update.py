#!C:\Users\tjsvl\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi,os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['description'].value

with open('data/'+pageId, 'w') as f:
    f.write(description)

os.rename('data/'+pageId, 'data/'+title)
#ReDirection
print("Location: index.py?id=" + title)
print()
