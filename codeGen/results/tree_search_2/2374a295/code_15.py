def is_divisible(n, i):
    return n % i == 0

def count_good_sequences(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, k + 1):
        if is_divisible(n, i):
            for j in range(i, k + 1):
                dp[j] += dp[j - i]
        else:
            break
    return dp[k] % 100000007

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
