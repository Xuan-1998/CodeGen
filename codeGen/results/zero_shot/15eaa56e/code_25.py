n, m = map(int, input().split())  # read number of rows and columns
table = [[int(x) for x in input().split()] for _ in range(n)]  # read table
k = int(input())  # read number of tasks

sorted_cols = [set() for _ in range(k)]
ans = "No"

for i, (l, r) in enumerate(map(int, input().split()) for _ in range(k)):
    col = [table[j][i] for j in range(l-1, r)]
    if all(col[j] <= col[j+1] for j in range(len(col)-1)):
        sorted_cols[i].add(i)

for cols in sorted_cols:
    if cols:
        ans = "Yes"
        break

print(ans)
