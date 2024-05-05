# Step 1: Read the input table, number of rows and columns, and number of tasks
n, m = map(int, input().split())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

k = int(input())

# Step 2: Iterate over each task and check if the subtable is sorted
for l, r in [list(map(int, input().split())) for _ in range(k)]:
    for col in range(m):
        if not all(table[i][col] <= table[i+1][col] for i in range(l-1, r)):
            print("No")
            break
    else:
        print("Yes")
