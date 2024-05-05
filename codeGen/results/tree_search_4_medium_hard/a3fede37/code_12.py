import sys
from collections import defaultdict

def max_path_sum(arr):
    n = len(arr)
    dp = [0] * (2 * n - 1)
    children = defaultdict(list)

    for i in range(n):
        if arr[i] > 0:
            left_child, right_child = 2*i + 1, 2*i + 2
            children[left_child].append(right_child)
            children[right_child].append(left_child)

    def dfs(node, parent_sum):
        nonlocal max_sum
        if node >= n:
            return

        dp[node - 1] = max(dp[node - 1], arr[node - 1] + parent_sum)

        for child in children[node]:
            dfs(child, dp[child - 1])

    max_sum = 0
    dfs(0, 0)
    return max_sum

input_arr = list(map(int, input().split()))
print(max_path_sum(input_arr))
