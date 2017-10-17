import math

n = int(input())
g = 9.81
for i in range(n):
    v0, angleInDegree, x1, h1, h2 = input().split()

    v0 = float(v0)
    angleInDegree = float(angleInDegree)
    x1 = float(x1)
    h1 = float(h1)
    h2 = float(h2)

    #gap = h2 - h1

    angleInRad = math.radians(angleInDegree)

    time = x1 / (math.cos(angleInRad)*v0)
    yDistance = (v0*time*math.sin(angleInRad)) - ((1/2)*g*time**2)

    if yDistance >= h1+1 and yDistance <= h2-1:
        print("Safe")
    else:
        print("Not Safe")