print("вариант 7")
def f(s):
    return s[:len(s)//2].replace("п", "*") + s[len(s)//2:]
print(f(input()))

