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
table, google_results 
Columns: 
url_id - unique id for url resulted from search query
search_id - foreign key to searches for the unique search query number
url - url resulted from search 
*/
CREATE TABLE google_results
	(url_id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(2048) NULL, 
    search_id INT NOT NULL REFERENCES searches(search_id),
    raw_text TEXT NULL,
    PRIMARY KEY(url_id),
    FULLTEXT(raw_text)
) ENGINE=InnoDB;
COMMIT;

/*
table, bing_results 
Columns: 
url_id - unique id for url resulted from search query
search_id - foreign key to searches for the unique search query number
url - url resulted from search 
*/
CREATE TABLE bing_results
	(url_id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(2048) NULL, 
    search_id INT NOT NULL REFERENCES searches(search_id),
    raw_text TEXT NULL,
    PRIMARY KEY(url_id),
    FULLTEXT(raw_text)
) ENGINE=InnoDB;
COMMIT;

/*
table, yahool_results 
Columns: 
url_id - unique id for url resulted from search query
search_id - foreign key to searches for the unique search query number
url - url resulted from search 
*/
CREATE TABLE yahoo_results
	(url_id INT NOT NULL AUTO_INCREMENT, 
    url VARCHAR(2048) NULL, 
    search_id INT NOT NULL REFERENCES searches(search_id),
    raw_text TEXT NULL,
    PRIMARY KEY(url_id),
    FULLTEXT(raw_text)
) ENGINE=InnoDB;
COMMIT;

/*
table, duckduckgo_results
Columns: 
url_id - unique id for url resulted from search query
search_id - foreign key to searches for the unique search query number
url - url resulted from search 
*/
CREATE TABLE duckduckgo_results
	(url_id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(2048) NULL, 
    search_id INT NOT NULL REFERENCES searches(search_id),
    raw_text TEXT NULL,
    PRIMARY KEY(url_id),
    FULLTEXT(raw_text)
) ENGINE=InnoDB;
COMMIT;

