import sys

def solve(n, m):
    # Step 1: Convert the number n into a list of digits
    digits = [int(x) for x in str(n)]
    
    # Step 2: Apply m operations to each digit d
    for _ in range(m):
        new_digits = []
        carry = 0
        for d in digits:
            next_digit = (d + 1) % 10
            if carry > 0:
                next_digit += 1
                carry = 0
                if next_digit >= 10:
                    carry = 1
                    next_digit %= 10
            new_digits.append(next_digit)
        digits = new_digits
    
    # Step 3: Calculate the length of the resulting number modulo 10^9+7
    result_length = len(str(n))
    while len(str(n)) > 0 and n % 1000000007 == 0:
        n //= 1000000007
        result_length -= 1
    return result_length

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
