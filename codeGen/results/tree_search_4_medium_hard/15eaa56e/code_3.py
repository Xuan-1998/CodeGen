import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    l, r = map(int, input().split())
    
    # Check each column individually
    for j in range(m):
        col = [table[i][j] for i in range(l-1, r)]
        
        # Perform a simple sort on the subtable indices within that column
        if sorted(col) == col:
            print("Yes")
            sys.exit(0)
    
print("No")
