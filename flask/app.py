from flask import Flask, request, render_template
import backend.populate_database as populate_db
import backend.query_database as query_db
import backend.config as config

#creating flask app instance
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #get query from user input on frontend 
        query = request.form['query']
        #define engines to query from
        engines = config.engines.keys()
        #loop through each engine and populate the database based on the query and engine
        for engine in engines:
            print('Populating database for '+engine+'...')
            populate_db.populate_database(query,engine)
        #get the search results
        results = query_db.search(query)
        #taking only top 10 results
        if len(results)>10:
            return render_template('results.html', results=results[:10])
        #display HTML
        return render_template('results.html', results=results)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



