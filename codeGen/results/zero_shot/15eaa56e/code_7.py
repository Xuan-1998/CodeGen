n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

def is_column_sorted(column):
    return all(column[i] <= column[i+1] for i in range(len(column)-1))

for l, r in tasks:
    subtable = [row[i] for row in rows[l-1:r]]
    if any(not is_column_sorted(subtable)):
        print("No")
        exit()
print("Yes")
