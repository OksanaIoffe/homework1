print("задание 1")
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
print("  ")

print("задание 2")
n = int(input())
i = 2
while n %i != 0:
    i += 1
print(i)
print("  ")

print("задание 3")
N = int(input())
i = 2
while i * 2 <= N:
    i = i * 2
print(i)
print("  ")

print("задание 4")
x = int(input())
y = int(input())
i =1
while x < y:
    x*= 1.1
    i+= 1
print(i)
print("  ")

print("задание 5")
len = 0
while int(input()) != 0:
    len +=1
print(len)
print("  ")

print("задание 6")
count = 0
sum = 0
i = int(input())
while i !=0:
    sum += i
    count +=1
    i = int(input())
print(sum/count)
print("  ")

print("задание 7")
i = int(input())
count = 0
while i != 0:
    next = int(input())
    if next != 0 and i < next:
        count+=1
    i = next
print(count)
print("  ")

print("задание 8")
prev = -1
len = 0
max_len = 0
element = int(input())
while element != 0:
    if prev == element:
        len += 1
    else:
        prev = element
        max_len = max(max_len,len)
        len = 1
    element = int(input())
max_len = max(max_len, len)
print(max_len)


