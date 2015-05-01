import re, urllib
from nltk import tokenize, tag

def run_tagging(toTag):
    #data = urllib.urlencode({"text":toTag}) 
    #u = urllib.urlopen("http://text-processing.com/api/tag/", data)
    #the_page = u.read()
    #print the_page
    #print type(the_page)
    
    text = tokenize.word_tokenize(toTag)
    the_page = tag.pos_tag(text)
    
    print the_page
    #extract1= (re.findall(r'\w/.\w+',  the_page))
    #extract1= (re.findall(r'(?<=\w/).\w+',  the_page))
    print toTag
    
    #print extract1
    #extract2= (re.findall(r'[A-Z]',  extract1))
    
    return "Passed"

def tagging_all(allResults):
    allsearchtext = ""
    for rResult2 in allResults:
        allsearchtext+=" "+rResult2.get("title").encode('ascii', 'ignore')
        allsearchtext+=" "+rResult2.get("summary").encode('ascii', 'ignore')
        
    data = urllib.urlencode({"text":allsearchtext}) 
    u = urllib.urlopen("http://text-processing.com/api/tag/", data)
    the_page = u.read()
    print "test2"
    print the_page
    print type(the_page)
    
    #extract1= (re.findall(r'\w/.\w+',  the_page))
    extract1= (re.findall(r'(?<=\w/).\w+',  the_page))
    
    print extract1
    
    return "Passed"

def tagging_ranks(theList):
    
    importantWords = []

    upTo = len(theList)
    for i in range(0, upTo):
        
        print theList[i][0]
        poS = tag.pos_tag(tokenize.word_tokenize(theList[i][0]))
        print poS
        theList[i].append(poS[0][1])
        
        if theList[i][1]<4:
            break
        
    print theList
    
    for words in theList:
        if len(words) > 2:
            if words[2].startswith(('JJ', 'NN', 'RB', 'VB')):
                importantWords.append(words)
    
    print importantWords
    return "Passed"
    
    pass

    #anything starting with JJ
    #anything startting with NN
    #anythihng start with RB
    #anything sw VB










