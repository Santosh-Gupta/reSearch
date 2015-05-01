
import os

from nltk.internals import find_file, find_jar, config_java, java, _java_options
import nltk
import unicodedata
import locations

nltk.internals.config_java(locations.javaPath)
from nltk.parse import stanford

java_path = locations.javaPath

os.environ['JAVAHOME'] = locations.javaPath
os.environ['STANFORD_PARSER'] = locations.stanfordParser
os.environ['STANFORD_MODELS'] = locations.stanfordModels

def stan_Parse(sentence_to_parse):

    parser = stanford.StanfordParser(model_path=locations.englishPCFG)
   
    print sentence_to_parse
    ready_to_parse = sentence_to_parse.encode("utf-8", "ignore")
    
    print type(ready_to_parse)
    print ready_to_parse
    
    sentences = parser.raw_parse((ready_to_parse))
    
    my_list = list(sentences)
    print type(my_list)
    print my_list
    
    return "passed"

#def stan_Depen(sentence_to_parse):
#    import StanfordDependencies
#    parser = stanford.StanfordParser(model_path=locations.englishPCFG)
#    sentences2 = parser.parse(("bring me a red ball",)) 
#    
#    sd = StanfordDependencies.get_instance(backend='subprocess')
#    print sd.convert_tree(str(sentences2))
#    
#    return "passed"
