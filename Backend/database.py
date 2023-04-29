import mysql.connector
import config
from mysql.connector import errorcode


def main():
    try:
    #get config MySQL parameters
        mySQLparams = config.mySQLparams
    #opening connection to MySQL database
        connection = mysql.connector.connect(user=mySQLparams['user'], database = mySQLparams['database'], password = mySQLparams['password'])
    #creating cursor handler for inserting data 
        cursor = connection.cursor()
        print("Database connected")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        connection.close()
