n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

# Check if any column is sorted
for j in range(m):
    for l, r in tasks:
        sorted_column = [x for i in range(l-1, r) for x in table[i][j]]
        if sorted_column != sorted(sorted_column):
            print("No")
            exit(0)

# If no unsorted subtables are found, then at least one column is sorted
print("Yes")
