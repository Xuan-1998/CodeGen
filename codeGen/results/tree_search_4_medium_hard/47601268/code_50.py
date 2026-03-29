===BEGIN CODE===
def solve(n):
    dp = [1]
    for i in range(1, n.bit_length() + 1):
        last_one_index = (i - 1) * 2
        prev_no_consecutive_ones_count = dp[i - 1] if i > 0 else 1
        curr_count = sum(dp[j] for j in range(last_one_index))
        dp.append(curr_count)
    return dp[-1]

n = int(input())
print(solve(n))
===END CODE===
