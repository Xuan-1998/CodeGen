n, m = map(int, input().split())
table = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))
    
for i in range(n):
    for j in range(m):
        if j > 0:
            table[i][j] = (table[i][j], table[i][j-1])
    
for l, r in tasks:
    for col in range(m):
        subtable = [x[col] for x in table[l-1:r]]
        if all(x <= y for x, y in zip(subtable, subtable[1:])):
            print("Yes")
            exit()
print("No")
