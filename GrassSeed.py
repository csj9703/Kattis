cost = input()
cost = float(cost)
areas = []
numOfLawn = int(input())
for x in range(numOfLawn):
    w,l = input().split()

    w = float(w)
    l = float(l)
    area = w*l
    areas.append(area)

tCost = sum(areas) * cost
print(tCost)
