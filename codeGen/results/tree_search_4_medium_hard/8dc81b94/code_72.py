def solve(n, total):
    if n == 0:
        return total == 0
    if dp[n] != -1:
        return dp[n]

    dp[n] = False

    for i in range(1, n+1):
        if (solve(i-1, total-n+i) or solve(n-i, total)) and all_equal(total-n+i):
            dp[n] = True
            break

    return dp[n]


def all_equal(total):
    for i in range(2, int(total**0.5)+1):
        if total % i == 0:
            return False
    return True


dp = [-1]*30001
for _ in range(int(input())):
    n = int(input())
    total = sum(map(int, input().split()))
    print("YES" if solve(n, total) else "NO")
