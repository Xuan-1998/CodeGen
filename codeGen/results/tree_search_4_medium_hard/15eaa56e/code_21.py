code
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for l, r in ([*map(int, input().split())] for _ in range(k)):
    sorted_col_exists = False
    for col in range(m):
        is_sorted = True
        for i in range(l-1, r):
            if table[i][col] > table[i+1][col]:
                is_sorted = False
                break
        if is_sorted:
            sorted_col_exists = True
            break
    print("Yes" if sorted_col_exists else "No")
