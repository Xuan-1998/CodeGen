import sys

def solve(n, m):
    # Apply operations until no more digits are increased
    while n > 0:
        new_n = 0
        carry = 1
        for digit in str(n):
            if int(digit) + carry >= 10:
                new_n += 1
                carry = 1
            else:
                new_n = new_n * 10 + (int(digit) + carry)
                carry = 0
        n = new_n
    # Return the length of the resulting number modulo 10^9+7
    return len(str(n)) % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
