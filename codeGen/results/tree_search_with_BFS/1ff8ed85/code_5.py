from sys import stdin, stdout

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    b = list(map(int, stdin.readline().split()))
    left = 1
    right = b[0]
    for i in range(1, n):
        if b[i] < left or b[i] > right:
            stdout.write("NO\n")
            break
        left = max(left, b[i])
        right += min(right, b[i-1]) - b[i]
    else:
        stdout.write("YES\n")

