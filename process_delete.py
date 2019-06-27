#!C:\Users\tjsvl\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi,os
form = cgi.FieldStorage()
pageId = form['pageId'].value


os.remove('data/'+pageId)

#ReDirection
print("Location: index.py")
print()
