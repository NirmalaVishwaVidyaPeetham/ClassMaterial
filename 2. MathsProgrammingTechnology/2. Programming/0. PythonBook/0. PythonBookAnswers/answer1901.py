s = "Hello, world!"
mask = (1<<5) | (1<<3) | (1<<1)    # 00101010

code = ""
for c in s:
    code += chr(ord(c)^mask)
print( code )

decode = ""
for c in code:
    decode += chr(ord(c)^mask)
print( decode )