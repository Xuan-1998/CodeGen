import sys

def read_input():
    T = int(input())
    for _ in range(T):
        N = int(input())
        yield N,

def calculate_expected_carries(N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        cumulative_sum = 0
        for j in range(i):
            if i - j > 1:
                cumulative_sum += min((10 ** (i - j - 1)) // 9, (10 ** i) // 9)
            else:
                cumulative_sum += min(1, (10 ** i) // 9)
        dp[i] = cumulative_sum + dp[i - 1]
    return sum(dp) / sys.maxsize

if __name__ == "__main__":
    for N in read_input():
        expected_carries = calculate_expected_carries(N)
        print(expected_carries)
