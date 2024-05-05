import sys

def alien_language(n, m):
    MOD = 10**8 + 7
    total_words = 1
    for i in range(m):
        if 2 * i <= n:
            letters_at_i = (n - i) * (n - i + 1) // 2
        else:
            letters_at_i = 1
        total_words *= letters_at_i % MOD
    return total_words

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
