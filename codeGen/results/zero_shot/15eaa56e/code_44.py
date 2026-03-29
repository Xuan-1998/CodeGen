n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
tasks = [[int(i) for i in input().split()] for _ in range(k)]

for task in tasks:
    l, r = task
    for col in range(m):
        subtable = [row[col] for row in table[l-1:r]]
        if not all(subtable[i] <= subtable[i+1] for i in range(len(subtable)-1)):
            break
    else:
        continue
    print("Yes")
    exit()

print("No")
