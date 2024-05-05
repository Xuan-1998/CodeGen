# Read the input values
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Initialize total joy with 0
total_joy = 0

# Sort the hares based on their maximum possible joy
sorted_hares = sorted(zip(a, b, c), key=lambda x: max(x[0], x[1], x[2]))

# Initialize left and right counts for feeding
left_count = 0
right_count = 0

# Iterate over the sorted hares
for i in range(n):
    # If left count is less than right count, feed from left
    if left_count < right_count:
        total_joy += a[i]
        left_count += 1
    # Else if right count is greater than or equal to left count, feed from right
    elif left_count >= right_count:
        total_joy += c[n - i - 1]
        right_count += 1

print(total_joy)
