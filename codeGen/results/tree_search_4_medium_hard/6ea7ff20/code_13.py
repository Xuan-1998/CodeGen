def can_merge(p):
    n = len(p) // 2

    # Initialize dynamic programming table with sentinel value (-1)
    dp = [-1] * (n + 1)

    # Base case: when i = n, check if the current permutation p matches either array a or b
    for i in range(n + 1):
        if i == n:
            if p[:i] not in dp and p[i:] not in dp:
                return "YES"
            else:
                return "NO"

    # Transition: add the next element from either array a or b to p
    for i in range(1, n + 1):
        j = len(p) - i
        if p[j] < p[i]:
            dp[i] = min(dp[i], dp[i-1]) + 1
        elif p[j] > p[i]:
            dp[i] = min(dp[i], dp[i+1]) + 1

    return "YES" if any(dp[:n+1]) else "NO"

while True:
    n = int(input())
    p = list(map(int, input().split()))
    print(can_merge(p))
