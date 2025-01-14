import re

mlist = re.finditer(r"a+","A sheep says 'baaaaah' to Ali Baba.")
for m in mlist:
    print( "{} is found at {}.".format(m.group(), m.start()))