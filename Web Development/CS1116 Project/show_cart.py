#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

result = ''
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if not http_cookie_header:
        sid = sha256(repr(time()).encode()).hexdigest()
        cookie['sid'] = sid
    else:
        cookie.load(http_cookie_header)
        if 'sid' not in cookie:
            sid = sha256(repr(time()).encode()).hexdigest()
            cookie['sid'] = sid
        else:    
            sid = cookie['sid'].value

    session_store = open('sess_' + sid, writeback=True)

    if len(session_store) == 0:
        result = '<p>No items in shopping cart.</p>'
    else:
        connection = db.connect('localhost', 'userid', 'password', 'database_name')
        cursor = connection.cursor(db.cursors.DictCursor)
        result = """<table>
                    <tr><th colspan="2">Your Cart</th></tr>
                    <tr><th>Wine</th><th>Quantity</th></tr>"""
        for wine_id in session_store:
            cursor.execute("""SELECT name FROM wines 
                               WHERE wine_id = %s""", (wine_id))
            row = cursor.fetchone()
            result += '<tr><td>%s</td><td>%s</td></tr>' % (row['name'], session_store.get(wine_id))
        result += '</table>'
        cursor.close()  
        connection.close()
 
    session_store.close()
    print(cookie)
except (db.Error, IOError):
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
    
print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Shrine of Bacchus Wines</title>
        </head>
        <body>
            %s
            <p>
                <a href="show_catalog.py">Show catalog</a>
            </p>
        </body>
    </html>""" % (result))