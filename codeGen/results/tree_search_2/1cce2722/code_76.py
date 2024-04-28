def delete_elements(a):
    n = len(a)
    memo = {0: 0}

    def dp(i):
        if i not in memo:
            if all(x == a[i] for x in a[:i+1]):
                memo[i] = 1
            else:
                memo[i] = max(dp(i-1), 1 + dp(i-2))
        return memo[i]

    return dp(n-1)

# Example usage:
n = int(input())
a = list(map(int, input().split()))
print(delete_elements(a))
