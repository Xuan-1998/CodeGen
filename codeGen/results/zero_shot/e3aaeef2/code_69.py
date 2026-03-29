import sys

def solve(n, m):
    # Apply operations and count the number of digits
    result = n
    for _ in range(m):
        new_digits = 0
        for digit in str(result):
            if int(digit) == 9:
                new_digits += 2
            else:
                new_digits += 1
        result = str(int(str(result)) + new_digits)
    
    # Return the length of the resulting number modulo 10^9+7
    return len(result) % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
