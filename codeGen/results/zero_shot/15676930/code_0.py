import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

# Initialize variables to keep track of fed hares and total joy
fed_hares = [False] * n
total_joy = 0

for i in range(n):
    if not fed_hares[i]:  # If hare is hungry
        if i == 0:  # First hare
            total_joy += a[0]
        elif i == n - 1:  # Last hare
            total_joy += c[-1]
        else:
            total_joy += max(a[i], b[i])
    fed_hares[i] = True

print(total_joy)
