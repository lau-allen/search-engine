#import libraries 
import inquirer
import populate_database
import query_database

#by Allen and Syed

#function to prompt user to chose a script 
def get_script():
    #define script options 
    script_options = [inquirer.List('Script',
                                    message='Choose Script',
                                    choices=['populate_database.py','query_database.py']
                                    )]
    #prompt user
    script = inquirer.prompt(script_options)
    #return chosen script
    return script['Script']


def main():
    
    #get chosen script
    script = get_script()

    #run script's main file when chosen 
    if script == 'populate_database.py':
        populate_database.main()
    elif script == 'query_database.py':
        query_database.main()

    return
    


if __name__ == '__main__':
    main()