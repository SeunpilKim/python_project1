#!C:\Users\tjsvl\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html; charset=utf-8\n")    # HTML is following
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form: #id라는게 form안에 있을 경우에 true
    pageId = form['id'].value
    with open('data/'+pageId) as f:
        description = f.read()
else:
    pageId = 'Welcome'
    description = 'Hello Web'
print('''<!doctype html>
<html>
<head>
<title>WEB1 - Welcome</title>
<meta charset="utf-8">
</head>
<body>
<h1><a href="index.py">WEB</a></h1>
<ol>
{list}
</ol>
<a href="create.py">create</a>
<form action="process_create.py" method="post">
    <p><input type="text" placeholder="title" name="title"></p>
    <p><textarea rows="4" placeholder="description" name="description"></textarea></p>
    <p><input type="submit"></p>
</form>
<body>
</html>
'''.format(title=pageId, content=description, list=view.getList()))
