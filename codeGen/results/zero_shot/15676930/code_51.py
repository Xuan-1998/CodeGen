# Step 1: Read the input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Step 2: Calculate the maximum joy for each hare based on its adjacent hares' states
max_joy = [0] * n

for i in range(n):
    if i == 0:
        max_joy[i] = c[i]
    elif i == n-1:
        max_joy[i] = c[i]
    else:
        max_joy[i] = max(c[i], b[i-1] + a[i])

# Step 3: Sort the hares based on their maximum joy values
sorted_hares = sorted(enumerate(max_joy), key=lambda x: x[1], reverse=True)

# Step 4: Calculate the total maximum joy by summing up the maximum joys of the sorted hares
total_max_joys = sum(hare[1] for hare in sorted_hares)

print(total_max_joys)
