import urllib 

def run_tagging(title):
    data = urllib.urlencode({"text":title}) 
    u = urllib.urlopen("http://text-processing.com/api/tag/", data)
    the_page = u.read()
    print the_page
    return "Passed"