fp = open( "pc_jabberwocky.txt" )
count = 0
while count < 5:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer, end="" )
    count += 1
fp.close()