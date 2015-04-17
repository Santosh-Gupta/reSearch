
import json
import urllib
import urllib2
#from urllib2 import Request, urlopen, URLError

def run_theasaurus(word):
    site = "http://words.bighugelabs.com/api/2/8155ed2c1e5dcd7d24a0aa41853092c7/"+word+"/json"
    request = Request(site)
    
    try:
            response = urlopen(request)
            kittens = response.read()
            print kittens
    except URLError, e:
        print 'No kittez. Got an error code:', e
        
    print type(response)
    
    #json_object = json.load(response)
    
    #json_object['syn']
    req = urllib2.Request(site)
    response = urllib2.urlopen(req)
    json_object = json.load(response)
    
    print json_object['noun']['syn'][2]
    print type(json_object)