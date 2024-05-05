def min_sum_marks(n, marks):
    memo = {0: 0}

    def dp(i):
        if i not in memo:
            total_marks = sum(marks[:i])
            prev_min = float('inf')
            for j in range(i):
                if marks[j] < i:
                    prev_min = min(prev_min, dp(j) - marks[j] + (i - j))
            memo[i] = prev_min + total_marks
        return memo[i]

    return dp(n)

# Example usage
n = int(input())
marks = list(map(int, input().split()))
print(min_sum_marks(n, marks))
