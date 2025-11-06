# this function computes (a+(b*c))-(a/(b+c)) with a, b, c as different floating point parameters. The function is called below 10 times.
def floating_point_expressions(a, b, c):
    answer = (a+(b*c))-(a/(b+c))
    return answer

t = floating_point_expressions(a=2.34, b=9.4, c=7.987)
print('floating_point_expressions(a=2.34, b=9.4, c=7.987) =', t)

t = floating_point_expressions(a=2.84, b=11.4, c=7.218)
print('floating_point_expressions(a=2.84, b=11.4, c=7.218) =', t)

t = floating_point_expressions(a=2.8123, b=1981.4, c=7.2)
print('floating_point_expressions(a=2.8123, b=1981.4, c=7.2) =', t)

t = floating_point_expressions(a=28123.111, b=81.4, c=2.348)
print('floating_point_expressions(a=28123.111, b=81.4, c=2.348) =', t)

t = floating_point_expressions(a=23.11, b=8.4, c=2.3)
print('floating_point_expressions(a=23.11, b=8.4, c=2.3) =', t)

t = floating_point_expressions(a=238.1, b=8.9874, c=23.98)
print('floating_point_expressions(a=238.1, b=8.9874, c=23.98) =', t)

t = floating_point_expressions(a=238.1765, b=8.12374, c=2398.111111)
print('floating_point_expressions(a=238.1765, b=8.12374, c=2398.111111) =', t)

t = floating_point_expressions(a=2381765.89, b=812374.7897, c=239811.7869)
print('floating_point_expressions(a=2381765.89, b=812374.7897, c=239811.7869) =', t)

t = floating_point_expressions(a=23865.52, b=2374.797, c=239.79)
print('floating_point_expressions(a=23865.52, b=2374.797, c=239.79) =', t)

t = floating_point_expressions(a=2386.2, b=74.7, c=9.7997)
print('floating_point_expressions(a=2386.2, b=74.7, c=9.7997) =', t)