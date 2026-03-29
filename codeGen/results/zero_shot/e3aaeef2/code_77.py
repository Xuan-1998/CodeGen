import sys

def get_length(n):
    len_n = 0
    while n > 0:
        n //= 10
        len_n += 1
    return len_n

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        new_n = 0
        while n > 0:
            digit = n % 10
            new_n = new_n * 10 + (digit + 1) % 10
            n //= 10
        n = new_n
    print(get_length(n) % (10**9 + 7))
