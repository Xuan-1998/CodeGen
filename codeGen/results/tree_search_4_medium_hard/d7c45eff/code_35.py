from typing import List

def min_string(n: int, k: int) -> str:
    dp = [[[] for _ in range(k + 1)] for _ in range(n + 1)]

    # Base case when i == 0
    for j in range(k + 1):
        if j < 1:
            dp[0][j] = ''
        else:
            dp[0][j] = 'a' * min(j, 1)

    # Recursive case when i > 0
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j < i:
                dp[i][j] = dp[i - 1][j]
            else:
                if j >= i:
                    delete_str = dp[i - 1][j - i]
                    dup_str = dp[i - 1][i] * (j // i)
                    if j % i > 0:
                        dup_str += 'a' * (j % i)
                    dp[i][j] = min(delete_str, dup_str)

    return dp[n][k]
