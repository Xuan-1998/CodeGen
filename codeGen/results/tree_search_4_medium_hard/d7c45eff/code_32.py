from collections import deque
import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    memo = {}

    def dfs(s, k):
        if (s, k) in memo:
            return memo[(s, k)]

        res = ''
        for _ in range(k):
            if not res or s[-1] <= 'z':
                res += s[-1]
                s = s[:-1]
            else:
                res += 'a'
                break

        memo[(s, k)] = res
        return res

    print(dfs(s, k))

if __name__ == "__main__":
    solve()
