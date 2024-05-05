import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

y_values = []
for i in range(n):
    x = 1
    y = 0
    operation = 1  # Initialize to increase both x and y
    while True:
        if operation == 1:  # Increase both x and y by a_x
            x += a[x]
            y += a[x]
            operation = 2  # Switch to the second operation
        elif operation == 2:  # Increase y by a_x while decreasing x by a_x
            y += a[x]
            x -= a[x]
            if x <= 0 or x > n:
                break
    y_values.append(y)

for i, y in enumerate(y_values):
    print(y)
