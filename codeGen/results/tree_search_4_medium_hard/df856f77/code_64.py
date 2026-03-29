import sys

def min_operations(A):
    n = len(A)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        if A[i - 1] > A[i]:
            dp[i] = dp[i - 1] + 1
        else:
            j = i - 1
            while j > 0 and A[j] >= A[i]:
                j -= 1
            dp[i] = dp[j + 1] + (i - j - 1)

    return dp[n]

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    print(min_operations(A))
