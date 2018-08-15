CREATE TABLE users
(
	username VARCHAR(20) NOT NULL,
	password VARCHAR(64) NOT NULL,
	email VARCHAR(64) NOT NULL,

	PRIMARY KEY (username)
);

CREATE TABLE comments_table 
(
    comment_id INT AUTO_INCREMENT,
    username VARCHAR(255),
    comment TEXT,
    PRIMARY KEY (comment_id)
);

CREATE TABLE vinyls 
(
    vinyl_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(5, 2) NOT NULL,
    genre VARCHAR(64) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (vinyl_id)
);