#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage
import pymysql as db

print('Content-Type: text/html')
print()

comments = ''
try:
    connection = db.connect('localhost', 'userid', 'password', 'database_name')
    cursor = connection.cursor(db.cursors.DictCursor)
    form_data = FieldStorage()
    if len(form_data) != 0:   
        username = form_data.getfirst('username')
        new_comment = form_data.getfirst('new_comment')
        cursor.execute("""INSERT INTO comments_table (username, comment)
                          VALUES (%s, %s)""", (username, new_comment))
        connection.commit()
    cursor.execute("""SELECT * FROM comments_table 
                      ORDER BY comment_id DESC""")
    for row in cursor.fetchall(): 
        comments += '<article><h1>%s</h1><p>%s</p></article>' % (row['username'], row['comment'])
    cursor.close()  
    connection.close()
except db.Error:
    comments = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>My Web Page</title>
        </head>
        <body>
            <p>
                Hello! This is my Web page!
            </p>
            <section>
                <h1>Comments</h1>
                <form action="page.py" method="post">
                    <fieldset>
                        <legend>Post a new comment</legend>
                        <label for="username">Name:</label>
                        <input type="text" name="username" id="username" />
                        <label for="new_comment">Comment:</label>
                        <textarea name="new_comment" id="new_comment" rows="5" cols="50">
                        </textarea>
                        <input type="submit" />
                    </fieldset>
                </form>
                %s
            </section>
        </body>
    </html>""" % (comments))