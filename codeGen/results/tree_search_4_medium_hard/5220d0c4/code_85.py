def min_prime_divisor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def is_good_prime(n):
    # Assuming good primes are greater than or equal to 5
    return n >= 5

def beauty_value(prefix, suffix):
    max_beauty = prefix[-1]
    for i in range(len(suffix) - 1, -1, -1):
        if is_good_prime(suffix[i]):
            max_beauty += min_prime_divisor(suffix[i])
        else:
            max_beauty -= min_prime_divisor(suffix[i])
    return max_beauty

n, m = map(int, input().split())
prefix = list(map(int, input().split()))
suffix = list(map(int, input().split()))

table = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    table[i][i] = beauty_value(prefix[:i], suffix[:i])

for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        table[i][j] = max(table[i][k] + table[k + 1][j] for k in range(i, j))

print(table[1][n])
