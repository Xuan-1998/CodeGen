import sys

def expected_carries():
    T = int(sys.stdin.readline())
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            return 0

        carry_prob = 1 / 10
        result = dp(i-1, j-1)
        for k in range(j+1):
            result += carry_prob * (10 ** (N - i - k))
        memo[(i, j)] = result
        return result

    for _ in range(T):
        N = int(sys.stdin.readline())
        print(sum(dp(N-i, i) for i in range(N+1)) / (2 ** N))

if __name__ == "__main__":
    expected_carries()
