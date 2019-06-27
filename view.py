import os
from html_sanitizer import Sanitizer

def getList():
    sanitizer = Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=sanitizer.sanitize(item))
    return listStr
