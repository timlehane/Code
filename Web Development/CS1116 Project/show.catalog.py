#!/usr/local/bin/python3

from cgitb import enable
enable()

import pymysql as db

print('Content-Type: text/html')
print()

result = ''
try:
    connection = db.connect('localhost', 'userid', 'password', 'database_name')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT * FROM vinyls ORDER BY vinyl_id""")

    for row in cursor.fetchall():
        result += """<div class="vinyl-outer">
                        <div class="vinyl-card">
                        <div class="vinyl-image">
                            <img src="HomeWD1_files/disc-32390_1280.png">
                        </div>
                        <div class="vinyl-info">
                            <h5>%s</h5>
                            <h5>%s</h5>
                            <h5>%s</h5>
                            <h6>%s</h6>
                        </div>
        </div>
        </div>""" % (row['name'], row['artist'], row['genre'], row['price']
    result += '</table>'
    cursor.close()  
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
    
print("""<!DOCTYPE html>
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
        <li><a href="News.html">News</a></li>
    </ul>
</nav>

<nav id="filterProducts">
    <h3>Vinyl</h3>

    <div class="filter">
        <div class="filter2">
          <label>Filter by:</label>
          <select>
            <option value="/">All Jackets</option>
          </select>
        </div>
        <div class="filter2">
          <label>Sort by:</label>
          <select>
            <option value="/">Featured</option>
          </select>
        </div>
    </div>
</nav>
<main>
    <section class="flexContainer">
        %s
    </section>
</main>
<footer>
    <small id="footerInfo">All images used throughout the development of this website are licensed under the creative commons license - downloaded from https://pixabay.com. Website was developed for submission to CS1116 Web Devlopment II Module under the administration of Derek Bridge. Website developed by Tim Lehane</small>
</footer>
</body></html>""" % (result))