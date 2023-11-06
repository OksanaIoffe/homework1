from math import sqrt, ceil
print("вариант 5")
A = 2
B = 4
C = 2
D = 6

chisl = A * D + B * C
znam = B * D

a, b = chisl, znam

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(f'{chisl // a}/{znam // a}')

def Del(n):
    p = []
    l = ceil(sqrt(n))
    for x in range(2, l):
        if n%x == 0:
            p.append(x)
            p.append(n//x)
    if sqrt(n).is_integer():
        p.append(sqrt(n))
    p.sort()
    return p
n = 30
print(n)
print(Del(n))
