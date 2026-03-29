n, m = map(int, input().split())  # read number of rows and columns
k = int(input())  # read number of tasks
tasks = []  # store task indices

for _ in range(k):
    l, r = map(int, input().split())  # read task indices
    tasks.append((l, r))

rows = [list(map(int, input().split())) for _ in range(n)]  # read table of integers
for task in tasks:
    l, r = task
    subtable = [row[l-1:r] for row in rows[l-1:r]]  # extract subtable
    if is_sorted_subtable(subtable):  # check sorting
        print("Yes")  # output "Yes" if sorted
    else:
        print("No")  # output "No" if not sorted

def is_sorted_subtable(subtable):
    return all(subtable[i][j] <= subtable[i+1][j] for i in range(len(subtable)-1) for j in range(m))
