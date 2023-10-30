print("вариант 5")
N = [10, -11, -23, -11, 11, -9, -8, 9, 3, 1111]
Otr = []
for i in range(1, len(N)-1):
    if N[i] < 0 and N[i+1] <0:
        Otr.append(N[i])
        Otr.append(N[i+1])
print(Otr)


K = [10, 33, 44, 93, 230, 93, 33, 91, 10, 33]
K2 = list(set(K))
print(K2)
