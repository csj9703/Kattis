h,m = input().split()
h = int(h)
m = int(m)

m = m - 45
if m < 0:
    h = h - 1
    if h < 0:
       h = h + 24
    else:
        pass
    m = m + 60
else:
    pass
print(h,m)

