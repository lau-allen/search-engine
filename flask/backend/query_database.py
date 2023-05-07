#importing libaries
import backend.config as config
import mysql.connector
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#function for connecting the database
def get_db_connection():
    #get params for connecting to DB 
    mySQLparams = config.mySQLparams
    #connect to DB
    connection = mysql.connector.connect(
        host = mySQLparams['host'],
        user = mySQLparams['user'],
        password = mySQLparams['password'],
        database = mySQLparams['database']
    )
    #return connect object 
    return connection


#function for removing stopwords from passed text 
def remove_stop_words(text,stop_words):
    tokens = word_tokenize(text)
    return [w for w in tokens if not w.lower() in stop_words]

#function to count the occurrences of keywords 
def keyword_count(keywords,text):
    kw_dict = dict()
    c = Counter(s.lower() for s in text.split())
    for term in keywords:
        kw_dict[term] = c[term.lower()]
    return kw_dict

def dict_to_tuple(d):
    keys = list(d.keys())
    values = list(d.values())
    sum_counts = sum(values)
    return sorted(tuple(zip(keys,values)),key=lambda x: -x[1]),sum_counts

#function for performing search in the mysql database using match function 
def search(query): 
    #get connection 
    connection = get_db_connection()
    #get cursor for executing commands with SQL DB 
    cursor = connection.cursor()
    #query 
    cursor.execute('SELECT url, website_title, raw_text  FROM search_results WHERE MATCH (raw_text) AGAINST(\''+query+'\' IN NATURAL LANGUAGE MODE)' )     #text is limited to 300 character from raw text
    #get all results
    results = cursor.fetchall()
    
    #logic for ranking search results 
    #downloading necessary NLTK data
    nltk.download('stopwords')
    nltk.download('punkt')
    #get stop_words from NLTK
    stop_words = set(stopwords.words('english'))
    #get keywords from query 
    query_keywords = remove_stop_words(query,stop_words)
    #perform keyword operations and formatting on results 
    results = list(map(lambda x: (x[0],x[1],x[2][:300]+'...',dict_to_tuple(keyword_count(query_keywords,x[2]))),results))
    #sort by decending keyword count order 
    results = sorted(results,key=lambda x: -x[3][1])

    #close cursor and connection
    cursor.close()
    connection.close()
    
    #return results 
    return results