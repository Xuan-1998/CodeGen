n = int(input())
m = int(input())
k = int(input())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

for l, r in tasks:
    for j in range(m):
        column = [row[j] for row in table[l-1:r]]
        is_sorted = all(column[i] <= column[i+1] for i in range(len(column)-1))
        if is_sorted:
            print("Yes")
            break
    else:
        print("No")
