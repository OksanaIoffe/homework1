print("Задание 1")  #я не знаю, нужны ли разграничения между заданиями практической, но для удобства я их сделала
A = 100
B = 110
while A<=B:
    print(A)
    A+=1
print("   ")

print("задание 2")
A = int(input())
B = int(input())
if A <= B:
    while A<=B:
        print(A)
        A+=1
else:
    while A >= B:
        print(A)
        A-=1
print("  ")

print("задание 3")
A = 10
B = 21
while A <= B:
    if A %2 !=0:
        print(A)
        A+=1
    else:
        A += 1
print("  ")

print("Задание 4")
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
print("  ")

print("задание 5")
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)
print("  ")

print("задание 6")
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)
print("  ")

print("задание 7")
n = int(input())
res = 1
sum = 0
for i in range(1, n + 1):
    res *= i
    sum += res
print(sum)
print("  ")

print("задание 8")
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
print("  ")

print("задание 9")
def task(n):
    s, c, p = 0, 0, 1
    for _ in range(n):
        c, p = c + p, c
        s += c
    return s
n = int(input("n="))
print(task(n))
print("  ")

print("задание 10")


