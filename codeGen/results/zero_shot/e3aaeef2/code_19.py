python
# Step 4: Calculate and print the result
def calculate_length(n, m):
    while m > 0:
        temp = 0
        while n > 0:
            digit = n % 10
            temp = temp * 10 + (digit + 1) % 10
            n //= 10
        n = temp
        m -= 1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print((str(calculate_length(n, m)) or '0').count('0'))
