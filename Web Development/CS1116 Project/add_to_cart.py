#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage 
from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

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

    # Get the id of the item being added to the cart
    form_data = FieldStorage()
    wine_id = form_data.getfirst('wine_id')

    # If this item is not in the cart already, then quantity is 1; otherwise, increment the quantity.
    qty = session_store.get(wine_id)
    if not qty:
        qty = 1
    else:
        qty +=1
    session_store[wine_id] = qty
    session_store.close()

    print(cookie)
    result = '<p>Item successfully added to your cart.</p>'
except IOError:
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
                <a href="show_cart.py">Show cart</a>
            </p>
            <p>
                <a href="show_catalog.py">Show catalog</a>
            </p>
        </body>
    </html>""" % (result))