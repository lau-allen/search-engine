#define dictionary to store search options: Google, Bing, Yahoo, DuckDuckGo 
engines = {'Google':'http://google.com/search?q=',
           'Bing':'https://www.bing.com/search?q=',
           'Yahoo':'https://search.yahoo.com/search?p=',
           'DuckDuckGo':'https://html.duckduckgo.com/html/?q='
           }

#list of engines that use javascript
js_engines = ['DuckDuckGo']

#list of urls to exclude from search engine results 
block_list = ['https://www.bing.com/new/termsofuse','https://privacy.microsoft.com/en-us/privacystatement',
              'https://account.microsoft.com/account/privacy','https://creativecommons.org/licenses/by-sa/3.0',
              'http://go.microsoft.com/fwlink/','https://go.microsoft.com/fwlink','https://support.microsoft.com',
              'http://support.google.com','http://policies.google.com','https://accounts.google.com',
              'http://www.google.com/preferences','setprefs?hl=en&prev=','https://search.yahoo.com/preferences',
              'https://mail.yahoo.com/','https://www.yahoo.com/news','https://finance.yahoo.com',
              'https://sports.yahoo.com/fantasy','https://sports.yahoo.com','https://shopping.yahoo.com',
              'https://www.yahoo.com/news/weathe','https://www.yahoo.com/lifestyle','https://help.yahoo.com/kb/search-for-desktop',
              'http://maps.google.com/maps','https://login.yahoo.com?.src=search','https://images.search.yahoo.com/search',
              'https://video.search.yahoo.com/search','https://search.yahoo.com/search?ei=UTF-8&','https://yahoo.uservoice.com/forums',
              'https://legal.yahoo.com/','https://guce.yahoo.com/privacy-dashboard','https://help.yahoo.com',
              'https://www.yahoo.com','https://www.google.com/imgres','https://www.google.com/maps','//duckduckgo.com/feedback.html'
             ]

#list of urls pertaining to ads to exclude from search engine results
ad_block_list = ['http://www.google.com/aclk','help.ads.microsoft',
                 'https://help.ads.microsoft.com','https://advertising.yahoo.com'
                ]

#parameters for MySQL connector to defined database 
mySQLparams = {'user':'root','database':'SEARCH_ENGINE_DB','password':'root'}

#sql query for inserting data into searches table 
add_search = ('INSERT INTO searches(query,engine) values(%s, %s)')

#sql query for inserting url and text data into search_results tabel
add_search_results = 'INSERT INTO search_results(url,search_id,raw_text) values(%s,%s,%s)'

#query for finding relevant URLs and info from query input using MySQL Full-Text Search 
def get_info(query):
    return 'SELECT url FROM search_results WHERE MATCH (raw_text) AGAINST(\''+query+'\' IN NATURAL LANGUAGE MODE)' 
    