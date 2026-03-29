from collections import defaultdict

def can_form_polygon(n, moods):
    memo = defaultdict(bool)
    dp = [False] * n
    dp[0] = True  # base case: only one knight left

    for i in range(1, n):
        for j in range(i):  # consider all previous knights
            if (moods[j] != moods[i-1]) and dp[j]:  # good mood alternates
                dp[i] = True
                break
        if not dp[i]:
            memo[(i, i-1)] = False  # memoize subproblem

    return "YES" if dp[-1] else "NO"

n = int(input())
moods = list(map(int, input().split()))
print(can_form_polygon(n, moods))
