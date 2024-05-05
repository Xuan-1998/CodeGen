n, m, k = map(int, input().split())
tasks = [list(map(int, input().split())) for _ in range(k)]

columns = [[int(x) for x in row.split()] for row in input().split()]
for i in range(m):
    columns[i] = sorted(columns[i])

for l, r in tasks:
    for i in range(l-1, r):
        if columns[i][r-l+1] < columns[i+1][0]:
            print("No")
            exit()
print("Yes")
