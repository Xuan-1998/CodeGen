def can_obtain_b(b):
    n = len(b)
    dp = {i: True for i in range(n + 1)}
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]
        if i < 0:
            return False
        if not dp[i]:
            return False
        odd_lengths = sum(l % 2 for l in b[:i+1]) % 2
        even_lengths = sum(l // 2 for l in b[:i+1]) % 2
        if odd_lengths and even_lengths:
            return False
        memo[i] = True
        return True

    for i in range(n + 1):
        dp[i] = helper(i)

    return "YES" if dp[n] else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_obtain_b(b) else "NO")
