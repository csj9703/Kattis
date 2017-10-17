n = int(input())

for i in range(n):
    x = input()
    if "simon says" in x[0:11]:
        print(x[11:])
    else:
        print(" ")