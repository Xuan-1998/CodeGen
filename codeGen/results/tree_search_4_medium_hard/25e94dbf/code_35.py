from collections import defaultdict

def max_distance(commands, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = defaultdict(dict)

    def dfs(k, i):
        if k == 0:
            return i
        if i > k:
            return dfs(k, k)
        if (k, i) in memo:
            return memo[(k, i)]

        modified_commands = [c for c in commands[:i] + ["T" if c == "F" else "F" for _ in range(n - i)]]
        turn_around = sum([1 if c == "T" else 0 for c in modified_commands])
        forward_distance = i
        backward_distance = n - i

        dp[k][i] = max(dfs(k - 1, i - 1) + 1 if i > k // 2 else dfs(k - 1, i), key=lambda x: x)

        memo[(k, i)] = dp[k][i]
        return dp[k][i]

    return dfs(n, n)


n = int(input())
commands = input()
print(max_distance(commands, n))
