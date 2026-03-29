import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    l, r = map(int, input().split())
    
    for i in range(m):
        sorted_column = table[l-1][i] == min(table[i][j] for j in range(r-l+1))
        
        if not any(sorted_column):
            print("No")
            sys.exit(0)
    
print("Yes")
