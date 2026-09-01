def left_circular_shift(n, d, N=8):
    """
    Performs a left circular shift (rotation) of an integer n by d bits
    within a total bit width of N.
    """
    # Ensure rotation distance is within the bit width
    d = d % N
        # Rotating an N-bit number by N-bits gives the same number. Circular shift by any multiples of N number of bits also gives same original number. So only the remained d%N matters for circular shift.

    # 1. Shift left. % (1 << N) acts as a mask to keep only N bits.
    rotated_left_part = (n << d) % (1 << N)
            # After this step N-d of the original bits remain at the left most end
    # 2. Shift right to catch the bits that "fell off" the left.
    rotated_right_part = (n >> (N - d))
            # You want to keep the first d original bits at the right end, so you right shift by N-d
    return rotated_left_part | rotated_right_part
def right_rotate(n, d, N=8):
    """
    Performs a right circular shift (rotation) of an integer n by d bits
    within a total bit width of N.
    """
    # Ensure rotation distance is within the bit width
    d = d % N
    # 1. Shift right.
    rotated_right_part = (n >> d)
            # Gives you the N-d left most bits of the original number
    # 2. Shift left to catch the bits that "fell off" the right.
    rotated_left_part = (n << (N - d)) % (1 << N)
            # We want the right most d bits of the original number,and want to keep them at the left most end
    return rotated_right_part | rotated_left_part

print(left_circular_shift(n=1101, d=2))
print(left_circular_shift(n=13, d=2))
print(right_rotate(n=1101, d=2))

print('---------------------------------')

print(f"12 & 7= {12&7}")
print(f"15 | 10= {15|10}")
print(f"20 ^ 13= {20^13}")
print(f"~10= {~10}")
print(f"8 << 2= {8<<2}")
print(f"64 >> 3= {64>>3}")
print(f"(5 & 3) | 4= {(5&3)|4}")
print(f"(10 >> 1) & 7= {(10>>1)&7}")
print(f"1 ^ 1 ^ 1= {1^1^1}")
print(f"~(-5)= {~(-5)}")

print(f"True or False and False= {True or False and False}")
print(f"not (True and False)= {not (True and False)}")
print(f"(5 > 3) and (2 == 2)= {(5 > 3) and (2 == 2)}")
print(f"0 or 5= {0 or 5}")
print(f"10 and 20= {10 and 20}")
print(f"not (apple == orange)= {not ("apple" == "orange")}")
a = True; b = True
print(f"(a = True; b = True) a != b= {a != b}")
print(f"8-bit circular left shift on 128 (10000000 in Base-2) by 1= {left_circular_shift(128, 1, 8)}")
print(f"bool(10) ^ bool(0)= {bool(10) ^ bool(0)}")
print(f"(7 & 1) == 1 and (8 >> 1) == 4= {(7 & 1) == 1 and (8 >> 1) == 4}")

print(f"True or False and not True= {True or False and not True}")
print(f"(23 > 42) and (36 > 12) or (39 <= 39)= {(23 > 42) and (36 > 12) or (39 <= 39)}")
print(f"10 + 5 << 1= {10 + 5 << 1}")
# can't do 9 simplifying problems
print(f"Can't do 9 simplifying problems. Ex., (A and B) or (A and not B)")
print(f"5 * 2 ** 2 & 15= {5 * 2 ** 2 & 15}")
print(f"not (15 // 3 == 5 and 7 % 2 == 0)= {not (15 // 3 == 5 and 7 % 2 == 0)}")

print(f"~5 & 7= {~5 & 7}")
print(f"1 << 3 | 1 << 1= {1 << 3 | 1 << 1}")
print(f"(True or False) and (not True or True)= {(True or False) and (not True or True)}")
print(f"8-bit circular right shift on 1 (00000001 in Base-2) by 1= {right_rotate(1, 1, 8)}")
print(f"not (5 < 2) or 10 // 2 == 5= {not (5 < 2) or 10 // 2 == 5}")