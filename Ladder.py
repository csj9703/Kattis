import math
h,v = input().split()
h = int(h)
v = int(v)
radian = math.radians(v)
answer = h/(math.sin(radian))
answer = int(answer) + 1
print(int(answer))