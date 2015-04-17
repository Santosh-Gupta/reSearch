from collections import Counter

def run_stats(search_results):
    
    allsearchtext = ""
    
    for rResult in search_results:
        allsearchtext+=" "+rResult.get("title").encode('ascii', 'ignore')
        allsearchtext+=" "+rResult.get("summary").encode('ascii', 'ignore')
    
    c = Counter()
    for line in allsearchtext.splitlines():
        c.update(line.lower().split())
        
    print allsearchtext 
    print(c)
        
    #print allsearchtext
    print "test"
    return "all clear"