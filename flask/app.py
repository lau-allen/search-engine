from flask import Flask, request, render_template
import mysql.connector

#creating flask app instance
app = Flask(__name__)

#function for connecting the database
def get_db_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = "root",
        database = "SEARCH_ENGINE_DB"
    )

    return connection


#function for performing search in the mysql database using match function 
def search(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT url, website_title, LEFT(raw_text, 300)  FROM search_results WHERE MATCH (raw_text) AGAINST(\''+query+'\' IN NATURAL LANGUAGE MODE)' )     #text is limited to 300 character from raw text
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results


# @app.route('/populate', methods=['GET', 'POST'])
# def populate():
#     if request.method == 'POST':
        
#         return "results after scraping search engine and populating database"
#     return "TO DO page to taking query to populate data"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = search(query)
        return render_template('results.html', results=results)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)



