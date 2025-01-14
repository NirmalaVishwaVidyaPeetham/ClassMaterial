import re

sentence = "Client: \"I wish to register a complaint! \
Hello miss!\"\n\
Shopkeeper: \"What do you mean, miss?\"\n\
Client: \"I am sorry, I have a cold.\"\n"

pspoken = re.compile( r"\"[^\"]*\"" )
spokenlist = pspoken.findall( sentence )
for text in spokenlist:
    print( text )