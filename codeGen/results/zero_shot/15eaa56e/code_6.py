# Read the input
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for task in range(k):
    l, r = map(int, input().split())
    
    # Check if the subtable is sorted in non-decreasing order
    for column in range(m):
        is_sorted = True
        for row in range(l-1, r):
            if table[row][column] > table[row+1][column]:
                is_sorted = False
                break
        if is_sorted:
            print("Yes")
            exit(0)
    
print("No")
