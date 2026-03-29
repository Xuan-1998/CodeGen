import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

total_joy = 0

for i in range(n):
    if i == 0:  # first hare
        total_joy += c[i]
    elif i == n - 1:  # last hare
        total_joy += a[i]
    else:
        if (a[i-1] + a[i+1]) % 3 == 1:  # both adjacent hares are hungry
            total_joy += b[i]
        elif (b[i-1] + c[i+1]) % 3 == 2:  # one adjacent hare is full and the other is hungry
            total_joy += a[i]
        else:  # both adjacent hares are full
            total_joy += c[i]

print(total_joy)
