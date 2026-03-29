n = int(input())  # Read n from stdin

a = list(map(int, input().split()))  # Read sequence a_2, ..., a_n
y_values = []

x = y = 1  # Initialize x and y
while True:  # Loop until program terminates
    x += a[x]
    y += a[x]
    x -= a[x]
    y += a[x]

    if x <= 0 or x > n:
        break

y_values.append(y)  # Store the final value of y for each sequence

for i, y in enumerate(y_values):
    print(y if i < len(y_values) - 1 else -1)  # Print the result
