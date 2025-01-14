import re

sentence = "William Randolph Hearst attempted to destroy all \
copies of Orson Welles' masterpiece 'Citizen Kane', because he \
did not appreciate the fact that the protagonist Charles \
Foster Kane was a thinly disguised caricature of himself. I \
wonder whether William Henry Gates The Third would attempt to \
do the same."

pname = re.compile( r"\b([A-Z][a-z]*(\s+[A-Z][a-z]*)+)\b" )
namelist = pname.finditer( sentence )
for name in namelist:
    print( name.group(1) )