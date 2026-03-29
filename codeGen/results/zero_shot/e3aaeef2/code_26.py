import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    result = str(n)
    for _ in range(m):
        temp = ''
        for digit in result:
            if digit == '9':
                temp += '1'
            else:
                temp += str(int(digit) + 1)
        result = temp
    print(len(result) % (10**9+7))
