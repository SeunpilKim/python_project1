#!C:\Users\tjsvl\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html; charset=utf-8\n")    # HTML is following
import cgi, os, view
from html_sanitizer import Sanitizer

sanitizer = Sanitizer()

form = cgi.FieldStorage()
if 'id' in form: #id라는게 form안에 있을 경우에 true
    title = pageId = form['id'].value
    with open('data/'+pageId) as f:
        description = f.read()
    #XSS.... BASIC
    # description = description.replace('<', '&lt;')
    # description = description.replace('>', '&gt;')
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)

    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
    description = 'Hello Web'
    update_link = ''
    delete_action = ''
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
{update_link}
{delete_action}
<h2>{title}</h2>
<p>{content}</p>
<body>
</html>
'''.format(title=title, content=description, list=view.getList(), update_link = update_link, delete_action=delete_action))
