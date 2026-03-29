import sys

def min_operations(A):
    n = len(A)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if A[i-1] <= A[i]:
            dp[i] = dp[i-1]
        else:
            insert_op = dp[i-1] + 1
            delete_op = 0 if i == 1 else dp[i-2] - (i - 1)
            dp[i] = min(insert_op, delete_op)

    return dp[-1]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(min_operations(A))
