#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

form_data = FieldStorage()
username = ''
result = ''
if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password = escape(form_data.getfirst('password', '').strip())
    if not username or not password:
        result = '<p>Error: user name and password are required</p>'
    else:
        sha256_password = sha256(password.encode()).hexdigest()
        try:
            connection = db.connect('localhost', 'userid', 'password', 'database_name')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users 
                              WHERE username = %s
                              AND password = %s""", (username, sha256_password))
            if cursor.rowcount == 0:
                result = '<p>Error: incorrect user name or password</p>'
            else:
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                   <p>Succesfully logged in!</p>
                   <p>Welcome back to Old School Vinylz.</p>
                   <ul>
                       <li><a href="protected_page_A.py">Old School Vinylz - Members Only A</a></li> 
                       <li><a href="protected_page_B.py">Old School Vinylz - Members Only B</a></li>
                       <li><a href="logout.py">Logout</a></li>
                   </ul>"""
                print(cookie)
            cursor.close()  
            connection.close()
        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        
print('Content-Type: text/html')
print()
print("""
<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Old School Vinylz</title>

    
    
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="HomeWD1_files/styles.css">    
</head>
<body>
<header>
    <h1>Old School Vinylz</h1>
    <p>An Online Shop for Vinyl Enthusiasts</p>
</header>
<nav>
    <ul>
        <li><a href="HomeWD1.html">Home</a></li>
        <li><a href="Shop.html">Shop</a></li>
        <li><a href="Interactive.html">Interactive</a></li>
        <li><a href="Checkout.html">Checkout</a></li>
        <li><a href="Logout.html">Logout</a></li>
    </ul>
</nav>
<main>
    <section id="intro">

        <img id="formImage" src="HomeWD1_files/turntable-1149496_1920.jpg" />
        <div id="formContainer">
        <form id="registerForm" action="register.py" method="post">
            <fieldset class="centre">
                <legend>Register</legend>
                <label for="username">Username</label>
                <input type="text" name="username"/>                
                <label for="email1">Email</label>
                <input type="email1" name="email1" />
                <label for="email2">Confirm email</label>
                <input type="email2" name="email2" />
                <label for="password1">Password</label>
                <input type="password1" name="password1" />
                <label for="password2">Confirm Password</label>
                <input type="password2" name="password2" />
            </fieldset>
            <fieldset class="centre">
                <input type="submit" value="Create Account" />
                <input type="reset"></input>
            </fieldset>
        </form>
        <form id="loginForm" action="login.py" method="post">
            <fieldset class="centre">
                <legend>Login</legend>
                <label for="username">Username</label>
                <input type="text" name="username"  value"%s"/>
                <label for="password">Password</label>
                <input type="password" name="password" />
            </fieldset class="centre">
            <fieldset>
                <input type="submit" value="Login" />
                <input type="reset"></input>
            </fieldset>
        </form>
        </div>
    </section>
    %s
</main>
<footer>
    <small id="footerInfo">All images used throughout the development of this website are licensed under the creative commons license - downloaded from https://pixabay.com. Website was developed for submission to CS1116 Web Devlopment II Module under the administration of Derek Bridge. Website developed by Tim Lehane</small>
</footer>
</body></html>""" % (username, result))