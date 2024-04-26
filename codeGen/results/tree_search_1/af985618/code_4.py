MOD = 998244353

def mod_binomial(n, k, mod):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

n = int(input().strip())
A = [input().strip().split() for _ in range(n)]

positive_elements = [(int(x), i) for i, (sign, x) in enumerate(A) if sign == '+']
answer = 0

for value, index in positive_elements:
    left_options = index
    right_options = n - index - 1
    for left_count in range(left_options + 1):
        for right_count in range(right_options + 1):
            if left_count + right_count == 0:
                continue
            ways = mod_binomial(left_options, left_count, MOD) * mod_binomial(right_options, right_count, MOD)
            ways %= MOD
            answer += value * ways * pow(2, left_count + right_count - 1, MOD)
            answer %= MOD

print(answer)
