from math import ceil, sqrt
print("блок А. 1")
def f(X, N):
    if N != 0:
        return (X**N)/N
X = int(input())
N = int(input())
print(f(X, N))

print("Блок Б. 1")
def max_():
    max_num = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num > max_num:
            max_num = num
    return max_num

print(max_())


