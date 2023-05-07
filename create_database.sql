/*
Search Engine DB 
*/
-- Create Database named SEARCH_ENGINE_DB
CREATE DATABASE SEARCH_ENGINE_DB; 
COMMIT;

-- define SEARCH_ENGINE_DB as database to perform actions on
USE SEARCH_ENGINE_DB;
/*
table, searches 
Columns: 
search_id - unique search query number 
query - string of query used in search 
engine - search engine used for query 
*/
CREATE TABLE searches
	(search_id INT NOT NULL AUTO_INCREMENT,
	query VARCHAR(255) NULL,
    engine VARCHAR(10) NOT NULL,
    PRIMARY KEY(search_id)
);
COMMIT;

/*
table, search_results 
Columns: 
url_id - unique id for url resulted from search query
search_id - foreign key to searches for the unique search query number
url - url resulted from search 
*/
CREATE TABLE search_results
	(url_id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(768) NULL, 
    search_id INT NOT NULL REFERENCES searches(search_id),
    website_title VARCHAR(2048) NULL,
    raw_text TEXT NULL,
    PRIMARY KEY(url_id),
    FULLTEXT(raw_text),
    UNIQUE(url)
) ENGINE=InnoDB;
COMMIT;


