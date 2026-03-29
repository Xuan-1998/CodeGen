import sys

def count_words(n, m):
    # Calculate the prefix sum for the first n letters
    prefix_sum = [1] * (n + 1)
    for i in range(1, n // 2 + 1):
        if 2 * i <= n:
            prefix_sum[2 * i] += prefix_sum[i]
    if n % 2 == 0:
        prefix_sum[n] += prefix_sum[n // 2]

    # Calculate the total number of possible words
    total_words = 1
    for _ in range(m):
        total_words = (total_words * prefix_sum[n % (_ + 1)]) % (10**8 + 7)
        n %= (_ + 1)

    return total_words

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
