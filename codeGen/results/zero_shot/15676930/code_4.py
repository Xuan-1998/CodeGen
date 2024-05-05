import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Step 1: Sort the hares by their joy values when both are hungry (ascending)
a.sort()
b.sort()

total_joy = 0
for i in range(n):
    # Step 2: If it's the first hare or the previous one was full, feed this one.
    if i == 0 or b[i-1] <= a[i]:
        total_joy += a[i]
    else:
        # Otherwise, feed the previous one and skip this one
        total_joy += b[i-1]

print(total_joy)
