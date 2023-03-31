#libraries
import inquirer
import mysql.connector
import config 

#function for prompting user to define query to search MySQL DB 
def get_query():
    #define inquirer question to prompt for query
    question = [inquirer.Text('query',message='Enter query')]
    #prompt user
    query = inquirer.prompt(question)
    #return query 
    return query['query'] 

def main():
    #get user defined query 
    query = get_query()

    #get config MySQL parameters
    mySQLparams = config.mySQLparams
    #opening connection to MySQL database
    connection = mysql.connector.connect(user=mySQLparams['user'], database = mySQLparams['database'], password = mySQLparams['password'])
    #creating cursor handler for inserting data 
    cursor = connection.cursor()

    #executing query to get related info from user defined query 
    cursor.execute(config.get_info(query))
    #return all records as a list of tuples 
    records = cursor.fetchall()

    #temporarily printing records; after this line; now that we have the records we can loop through the records to display on the UI
    print(records)

    #commit data to database 
    connection.commit()

    #closing cursor and connection 
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()

