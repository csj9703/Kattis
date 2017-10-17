import math

ans = []

n, w, h = input().split()
n = int(n)
w = int(w)
h = int(h)

for i in range(n):
  i = int(input())
  if i <= w or i <= h or i <= math.sqrt(math.pow(w, 2)+math.pow(h, 2)):
    ans.append("DA")
  else:
    ans.append("NE")
print ("\n".join(ans))