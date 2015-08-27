# reSearch
Takes search engine results and re ranks them. A work in progress. 

You need to alter the locations.py file (in /src/joins/locations.py). 

You need put a path to Java. You need Java 8 or above, including the development kit, which you can download here http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html.

You also need to link a location to the stanford parser, located at 
http://nlp.stanford.edu/software/stanford-parser-full-2015-04-20.zip
or you can go to their downloads page at http://nlp.stanford.edu/software/lex-parser.shtml#Download

You also need to link the location to a file named englishPCFG. The englishPCFG.ser.gz file can be 
found inside the models.jar file (/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz). 
Please use an archive manager to 'unzip' the models.jar file.

All locations are entered in the locations.py file. Please check to see that you have linked JAVA JDK 8.0 or above, a common problem is that people have linked a folder which has a previous version. 

Another common issue is that nltk doesn't come installed with all the appropiate programs. In that case refer to 
http://stackoverflow.com/questions/8590370/how-to-do-pos-tagging-using-nlp-pos-tagger-in-python
Keep in mind you can download any specific code directly ie running "nltk.download('maxent_treebank_pos_tagger')" in python

