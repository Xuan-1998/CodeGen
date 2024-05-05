from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def min_prime(n):
    for i in range(2, n+1):
        if is_prime(i):
            return i

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    memo = {}
    max_beauty = float('-inf')

    for i in range(n):
        if is_prime(arr[i]):
            min_divisor = min_prime(arr[i])
            v = min_divisor
        else:
            v = -1

        k = i
        while k >= 0 and (k not in memo or memo[k] <= max(0, v-1)):
            k -= 1
            if is_prime(arr[k]):
                min_divisor = min_prime(arr[k])
                v += min_divisor
            else:
                v -= 1

        memo[k] = v
        max_beauty = max(max_beauty, v)

    print(max_beauty)

solve()
