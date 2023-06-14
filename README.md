# Search Engine
The goal of this search engine is to provide a tool that compiles the search results from major engine services (Google, Bing, Yahoo, DuckDuckGo), such that it enables refined secondary searches from resultant first set of searches, reduces the bias of search results by introducing a keyword frequency ranking algorithm, and removes ads (which are given priority in engine services). 

# Steps to run Search Engine code
1. Create conda environment with required libraries: conda create --name <env> --file conda_requirements.txt
2. Launch MySQL Workbench and run create_database.sql script to create MySQL Database
3. Change directory to flask folder: cd flask 
4. Run search engine on local environment: python app.py 
  
# Major Files Breakdown
* create_database.sql - MySQL script for creating databases, including the tables for storing the searches and search results, constraints for primary keys, foreign key relationships, auto incrementing of primary key IDs, etc.
*	app.py - Entry point for the Foogle search engine, which calls the other scripts like the HTML, CSS, and Python scripts that make the project function 
*	populate_database.py - Logic for querying Google, Bing, Yahoo, DuckDuckGo, providing pipeline for retrieving data, cleaning data, etc. and populating the MySQL Database 
*	query_database.py - Logic for taking a user-input query, finding the relevant websites using natural language processing from the MySQL database, and returning a keyword sorted list of websites that are curated as the more relevant results to the user. 
*	conda_requirements.txt - dependencies file for creating conda environment to run project 
*	DSEI240_SearchEngine_AllenLau_SyedFaquaruddinQuadri.pdf - presentation 


