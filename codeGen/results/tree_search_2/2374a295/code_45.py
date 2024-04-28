def count_good_sequences(n, k):
    memo = {0: 1}  # base case: only one good sequence of length 0

    def dp(i):
        if i not in memo:
            memo[i] = sum(1 if j % i == 0 else 0 for j in range(1, n+1)) * dp(i-1) // (i-1)
        return memo[i]

    return pow(10, 9, 1000000007) * dp(n) % 1000000007

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
