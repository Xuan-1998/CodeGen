# Receive input
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# Initialize count of tasks that satisfy the condition
count = 0

for task in range(k):
    l, r = map(int, input().split())
    
    # Check if subtable is sorted in non-decreasing order
    for col in range(m):
        sorted_col = table[l-1][col] <= table[i][col] for i in range(l, r+1)]
        
        if not sorted_col:
            break
    else:
        count += 1

# Print the output
print("Yes" if count > 0 else "No")
