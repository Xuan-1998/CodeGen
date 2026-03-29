n, m = map(int, input().split())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)
k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

for l, r in tasks:
    for col in range(m):
        subtable = [row[col] for row in table[l-1:r]]
        is_sorted = all(subtable[i] <= subtable[i+1] for i in range(len(subtable)-1))
        if is_sorted:
            print("Yes")
            break
    else:
        print("No")
