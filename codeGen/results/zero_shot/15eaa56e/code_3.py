code block
for k in range(int(input())):
    l, r = map(int, input().split())
    for j in range(m):
        min_val = col_min[l-1][j]
        for i in range(l-1, r):
            if table[i][j] < min_val:
                print("No")
                exit()
        print("Yes" if all(table[i][j] >= min_val for i in range(l-1, r)) else "No")
