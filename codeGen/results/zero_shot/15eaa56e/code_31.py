# Step 1: Read the input
n, m = map(int, input().split())  # number of rows and columns
table = [list(map(int, input().split())) for _ in range(n)]  # read the table
k = int(input())  # number of tasks

# Step 2: Process each task
for l, r in [map(int, input().split()) for _ in range(k)]:  
    for col in range(m):  # iterate over each column
        subtable = [row[col] for row in table[l-1:r]]  # get the subtable for this task and column
        if sorted(subtable) == subtable:  # check if the subtable is sorted
            print("Yes")
            break  # if it's sorted, we don't need to check other columns
    else:
        print("No")  # if no column has a sorted subtable, then "No"
