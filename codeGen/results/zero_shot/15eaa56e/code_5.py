n, m = map(int, input().split())  
table = [list(map(int, input().split())) for _ in range(n)]  
k = int(input())  
tasks = []  
for _ in range(k):
    l, r = map(int, input().split())  
    tasks.append((l, r))  

for l, r in tasks:
    for j in range(m):  # iterate through each column
        col = [row[j] for row in table[l-1:r]]  # extract the subtable column
        if not all(col[i] <= col[i+1] for i in range(len(col)-1)):
            print("No")  
    print("Yes")
