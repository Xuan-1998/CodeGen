from typing import List

def read_input() -> List[int]:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b


def solve(n: int, a: List[int], b: List[int]) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == 1:
            dp[i][1] = a[0]
        elif i == 2:
            dp[i][1] = max(a[0], b[0])
            dp[i][2] = max(a[0] + b[0], a[1])
        else:
            for j in range(1, i + 1):
                if j == 1:
                    dp[i][j] = a[i - 1]
                elif j == 2:
                    dp[i][j] = max(dp[i-1][k-1] + a[i - 1], dp[i-1][k] + b[i - 1]) for k in range(min(j, i-1))
                else:
                    dp[i][j] = max(dp[i-1][k-1] + a[i - 1] if k > 0 and k < j else 0, 
                                   dp[i-1][k] + b[i - 1] if k > 0 else 0) for k in range(min(j, i-1))
        return dp[n][n]


if __name__ == "__main__":
    n, a, b = read_input()
    print(solve(n, a, b))
