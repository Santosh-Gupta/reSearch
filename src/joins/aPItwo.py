import re, urllib

def run_tagging(title):
    data = urllib.urlencode({"text":title}) 
    u = urllib.urlopen("http://text-processing.com/api/tag/", data)
    the_page = u.read()
    print the_page
    print type(the_page)
    
    #extract1= (re.findall(r'\w/.\w+',  the_page))
    extract1= (re.findall(r'(?<=\w/).\w+',  the_page))
    
    print extract1
    #extract2= (re.findall(r'[A-Z]',  extract1))
    
    return "Passed"