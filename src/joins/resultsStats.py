from collections import Counter
from aPITag import tagging_ranks

def run_stats(search_results):
    
    allsearchtext = ""
    
    for rResult in search_results:
        allsearchtext+=" "+rResult.get("title").encode('ascii', 'ignore')
        allsearchtext+=" "+rResult.get("summary").encode('ascii', 'ignore')
    
    listAllSearchText = allsearchtext.split()
    cnt = Counter()
    for word in listAllSearchText:
        cnt[word] += 1
    
    listCnt = list(cnt.items())
    sortedlistCnt = sorted(listCnt, key=lambda x: x[1], reverse=True)
    print sortedlistCnt
    print type(sortedlistCnt)
    print type(sortedlistCnt[0])
    
    for x in range(0, len(sortedlistCnt) ):
        sortedlistCnt[x]=list(sortedlistCnt[x])

    print type(sortedlistCnt[3])
    
    tagging_ranks(sortedlistCnt)
    #c = Counter()
    #for line in allsearchtext.splitlines():
    #    c.update(line.lower().split())
    #    
    #print allsearchtext
    #print(c)
    #print type(c)
        
    #print allsearchtext
    return "all clear"