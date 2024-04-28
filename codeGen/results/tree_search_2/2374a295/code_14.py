def is_divisible(n, k):
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

dp = {0: 1}

def count_good_sequences(n, k):
    if k not in dp:
        dp[k] = sum(count_good_sequences(i-1, k-i)*is_divisible(n, i) for i in range(1, k+1))
    return dp[k]

n, k = map(int, input().split())
print(count_good_sequences(n, k) % 1000000007)
