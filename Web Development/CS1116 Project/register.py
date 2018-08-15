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
    password1 = escape(form_data.getfirst('password1', '').strip())
    password2 = escape(form_data.getfirst('password2', '').strip())
    email1 = escape(form_data.getfirst('email1', '').strip())
    email2 = escape(form_data.getfirst('email2', '').strip())
    if not username or not password1 or not password2 or not email:
        result = '<p>Error: user name and passwords are required</p>'
    elif password1 != password2:
        result = '<p>Error: passwords must be equal</p>'
    elif email1 != email2:
        result = '<p>Error: emails must be equal</p>'
    else:
        try: #Begin Try
            connection = db.connect('localhost', 'userid', 'password', 'WD2_Vinyl')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s""", (username)) #Check if username is already taken
            if cursor.rowcount > 0:
                result = '<p>Error: user name already taken</p>'
            else:
                sha256_password = sha256(password1.encode()).hexdigest()
                cursor.execute("""INSERT INTO users (username, password, email) 
                                  VALUES (%s, %s)""", (username, sha256_password, email1))
                connection.commit()
                cursor.close()  
                connection.close()
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                   <p>Succesfully inserted!</p>
                   <p>Thanks for joining Old School Vinylz.</p>
                   <ul>
                       <li><a href="protected_page_A.py">Old School Vinylz - Members Only A</a></li> 
                       <li><a href="protected_page_B.py">Old School Vinylz - Members Only B</a></li>
                       <li><a href="logout.py">Logout</a></li>
                   </ul>"""
                print(cookie)
        except (db.Error, IOError): #Error
            result = '<p>Sorry! We are experiencing problems with our database. Please call back later.</p>'
        
print('Content-Type: text/html')
print()
print("""
<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Old School Vinylz</title>
    <script src="check_name_available.js"></script>
    
    
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
                <input type="text" name="username" value"%s"/>    
                <span id="checker"></span>
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
                <input type="text" name="username" />
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


# result = ''
# if the user is sending us data:
#     if username blank or passwords blank or passwords not equal:
#         result = error message
#     else:
#         if username already in database:
#             result = error message
#         else:
#             encrypt password
#             insert new user details in database
#             create a cookie containing a session id
#             store data about this user in session store
#             result = the 'protected' content
#             output the cookie
# output Web page containing form and 'result'