import math

x = 14.26
y = - 1.22
z = 3.5 * 10**(-2)

s = 2 * math.cos(x - 2/3) /( 1/2 + math.sin(y)**2) * (1 + ((z**2)/(3 - (z**2)/5)))
print("s ={0:.6f}".format(s))

x = 3.74* 10**(-2)
y = -0.825
z = 0.16*10**2

s = (1 + math.sin(x + y)**2) / (x -(( 2 * y)/ (1 + x**2 * y**2))) * x ** abs(y) + math.cos(math.atan(1/z))**2
print("s ={0:.5f}".format(s))

x = 0.1722
y = 6.33
z = 3.25*10**(-4)
s = 5 * math.atan(x) - 1/4 * math.acos(x) * (x + 3 * abs(x - y) + x**2)/(abs(x - y) * z + x**2)
print("s ={0:.3f}".format(s))