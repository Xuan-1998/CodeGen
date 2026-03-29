from typing import List

def min_cuts(s: str) -> int:
    n = len(s)
    dp: List[List[bool]] = [[False] * (n + 1) for _ in range(n + 1)]

    def is_palindrome(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if is_palindrome(i, j):
                dp[i][j] = True
            else:
                for k in range(i, j):
                    if not dp[i][k] or not dp[k + 1][j]:
                        dp[i][j] = True
                        break

    min_cuts = n - 1
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                min_cuts = min(min_cuts, j - i)

    return min_cuts
