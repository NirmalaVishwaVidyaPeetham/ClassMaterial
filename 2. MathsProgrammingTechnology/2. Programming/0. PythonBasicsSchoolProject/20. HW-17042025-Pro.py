# addition
def multiplication(x, y):
    print('multiplication: ', '\n')
    ans = 0
    for i in range(1, y+1):
        ans += x
        print(x, ' * ', i, ' =', ans)
    #print(x,' * ',y,' =', ans)
    return
multiplication(5, 7)
print('\n')

# multiplication
def power(x, y):
    print('power: ', '\n')
    i=1
    ans = 1
    while i < y+1:
        ans *= x
        print(x, ' ** ', i, ' =', ans)
        i += 1
    #print(x,' ** ',y,' =', ans)
    return
power(5, 3)