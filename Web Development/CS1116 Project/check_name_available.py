#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db
            
print('Content-Type: text/plain')
print()

form_data = FieldStorage()
username = escape(form_data.getfirst('username', '').strip())
try:    
    connection = db.connect('localhost', 'userid', 'password', 'database_name')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT * FROM users 
                      WHERE username = %s""", (username))
    if cursor.rowcount > 0:
        print('in_use')
    else:
        print('available')
    cursor.close()  
    connection.close()
except db.Error:
    print('problem')