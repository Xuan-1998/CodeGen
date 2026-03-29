n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(k):
    l, r = map(int, input().split())
    
    column_sorted = all(table[j][i] <= table[j+1][i] for j in range(l-1, r))
    print("Yes" if column_sorted else "No")
