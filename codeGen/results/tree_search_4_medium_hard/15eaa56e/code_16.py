import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for task in range(k):
    l, r = map(int, input().split())
    
    for column in range(m):
        sorted_column = table[l-1][column] == -1 and sorted([row[column] for row in table[l-1:r]]) or [table[i][column] for i in range(l-1,r)]
        
        if sorted_column != list(range(sorted_column[0], sorted_column[-1]+1)):
            print("No")
            sys.exit()
    
print("Yes")
