n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for task in range(k):
    l, r = map(int, input().split())
    
    for col in range(m):
        subtable = [row[col] for row in table[l-1:r]]
        
        if not all(subtable[i] <= subtable[i+1] for i in range(len(subtable)-1)):
            print("No")
            exit()
    
print("Yes")
