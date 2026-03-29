from collections import deque

def solve():
    n = int(input())
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    queue = deque([0])

    while queue:
        i = queue.popleft()
        for j in range(n):
            if j != i and dp[j] > dp[i] + 1:
                dp[j] = dp[i] + 1
                queue.append(j)

    min_inv = max(dp)
    capital_cities = [i for i, dist in enumerate(dp) if dist == min_inv]

    print(min_inv)
    print(' '.join(map(str, capital_cities)))

if __name__ == '__main__':
    solve()
