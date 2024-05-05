import heapq

def solve(n, q):
    signs = [1 if x == '+' else -1 for x in input().split()]
    dp = [[(0, 0, 0)] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        left, right, sign_sum = dp[i][i]
        dp[i][i+1] = [(left, right, sign_sum + signs[i])]
        if i > 0:
            dp[0][i] = [(0, i, signs[0] + sign_sum)]

    for i in range(n):
        for j in range(i, n):
            left, _, _ = dp[i][j]
            right, r, s = dp[j+1][n-1]
            if abs(s) > abs(left - right):
                left += 1
                right -= 1
            else:
                left -= 1
                right += 1

    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l, r))

    result = []
    while queries:
        l, r = heapq.heappop(queries)
        ans = float('inf')
        for i in range(l-1, r+1):
            left, right, sign_sum = dp[i][i]
            if sign_sum == 0:
                ans = min(ans, abs(left - right))
        result.append(min(result) if result else ans)

    return '\n'.join(map(str, result))

if __name__ == '__main__':
    n, q = map(int, input().split())
    print(solve(n, q))
