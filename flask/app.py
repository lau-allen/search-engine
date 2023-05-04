from flask import Flask, request, render_template
import mysql.connector
import backend.populate_database as populate
import backend.config as config

#creating flask app instance
app = Flask(__name__)

#function for connecting the database
def get_db_connection():
    mySQLparams = config.mySQLparams
    connection = mysql.connector.connect(
        host = mySQLparams['host'],
        user = mySQLparams['user'],
        password = mySQLparams['password'],
        database = mySQLparams['database']
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


@app.route('/populate', methods=['GET', 'POST'])
def populate():
    if request.method == 'GET':
        #get user input for query and search engine choice 
        query = request.form['query']
        search_engine = 'Google'
        results = search(query)
        #call populate database with input_query and search_engine choice 
        populate.populate_database(results,search_engine)
        #random code Allen put below. Need to replace with Adnan code. 
        return render_template('results.html', results=results)
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = search(query)
        return render_template('results.html', results=results)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



