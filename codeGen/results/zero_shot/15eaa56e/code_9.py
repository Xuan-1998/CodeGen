import sys

n, m = map(int, input().split())  # read number of rows and columns
k = int(input())  # read number of tasks
table = [list(map(int, input().split())) for _ in range(n)]  # read table

for task in range(k):
    l, r = map(int, input().split())  # read task indices (l, r)
    subtable = [row[l-1:r] for row in table[l-1:r]]  # extract subtable
    is_sorted = True
    for col in range(len(subtable[0])):
        for i in range(1, len(subtable)):
            if subtable[i][col] < subtable[i-1][col]:
                is_sorted = False
                break
        if not is_sorted:
            break
    if is_sorted:
        print("Yes")
        sys.exit()
print("No")
