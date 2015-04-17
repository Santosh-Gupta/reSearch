
import os

from nltk.internals import find_file, find_jar, config_java, java, _java_options
import nltk
import unicodedata

nltk.internals.config_java("C:/Program Files/Java/jre1.8.0_40/bin/java.exe")
from nltk.parse import stanford

java_path = "C:/Program Files/Java/jre1.8.0_40/bin/java.exe"
os.environ['JAVAHOME'] = java_path

def stan_Parse(sentence_to_parse):

    os.environ['STANFORD_PARSER'] = 'C:/Python34/lwc/stanford-parser-full-2015-01-30/stanford-parser.jar'
    os.environ['STANFORD_MODELS'] = 'C:/Python34/lwc/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models.jar'

    parser = stanford.StanfordParser(model_path="C:/Python34/lwc/stanford-parser-full-2015-01-30/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
   
    print sentence_to_parse
    ready_to_parse = sentence_to_parse.encode("utf-8", "ignore")
    
    print type(ready_to_parse)
    print ready_to_parse
    
    sentences = parser.raw_parse((ready_to_parse))
    
    my_list = list(sentences)
    print type(my_list)
    print my_list
    
    return "passed"

