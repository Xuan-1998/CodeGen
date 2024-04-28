def is_divisible(n, i):
    return n % i == 0

def good_sequences(n, k):
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i > n or k < 0:
            return 0

        if i == 0:
            return 1

        result = sum(dp(j-1, k-j)*is_divisible(n, j) for j in range(1, k+1))
        memo[(i, k)] = result
        return result

    return dp(1, k) % 1000000007

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(good_sequences(n, k))
