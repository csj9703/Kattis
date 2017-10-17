import math
a, n = input().split()
a = float(a)
n = float(n)

if n >= 2*math.pi*((a/math.pi)**(1/2)):
    print("Diablo is happy!")
else:
    print("Need more materials!")