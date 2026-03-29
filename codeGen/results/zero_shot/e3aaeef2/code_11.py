import sys

def solve(n, m):
    # Base case: single-digit number
    if n < 10:
        return n % (10**9 + 7)

    # Apply operations and update the length
    for _ in range(m):
        new_n = 0
        carry = 1
        while n > 0:
            digit = n % 10
            new_n = new_n * 10 + (digit + 1) % 10
            n //= 10
            if carry:
                new_n += 1
                carry = 0
        n = new_n

    # Return the length of the resulting number modulo 10^9+7
    return len(str(n)) % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
