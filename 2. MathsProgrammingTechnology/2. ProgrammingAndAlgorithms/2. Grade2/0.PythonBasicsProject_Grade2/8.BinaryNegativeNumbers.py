x = 0x00010111  # Hexadecimal notation
print(x)
print(1+16+16**2+16**4) # Verifying hexadecimal to decimal conversion
print(hex(65809))

y=0b00010111    # Binary notation
print(y)
print(1+2+2**2+2**4)

z=0b10010111    # Treats this as a positive integer only - python doesn't use two's complement form for negative integers. It uses sign-magnitude form.
print(z)
print(1+2+2**2+2**4+2**7)
print(bin(151))

p = -105
print(bin(p))
q = 105
print(bin(q))