# Read the input
n = int(input())
a_values = list(map(int, input().split()))
b_values = list(map(int, input().split()))
c_values = list(map(int, input().split()))

# Sort the values
a_sorted = sorted((val, i) for i, val in enumerate(a_values))
b_sorted = sorted((val, i) for i, val in enumerate(b_values))
c_sorted = sorted((val, i) for i, val in enumerate(c_values))

# Initialize variables to keep track of current joy and total joy
current_joy = 0
total_joy = 0

for a, b, c in zip(a_sorted, b_sorted, c_sorted):
    # Update the current joy based on the feeding order
    if len(set([a[1], b[1], c[1]])) == 3:  # If all hares are hungry
        current_joy = a[0]
    elif len(set([b[1], c[1]])) == 2:  # If one hare is full and the other is hungry
        current_joy = b[0]
    else:
        current_joy = c[0]

    total_joy += current_joy

print(total_joy)
