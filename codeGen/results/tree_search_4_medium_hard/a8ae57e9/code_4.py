import sys

def solve():
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    table_capacities = list(map(int, input().split()))
    for i in range(1, n + 1):
        group_size, group_spend = map(int, input().split())
        max_earn = 0
        for j in range(k):
            if table_capacities[j] >= group_size:
                earn = group_spend + dp[i - 1]
                max_earn = max(max_earn, earn)
                break
        dp[i] = max_earn
    
    accepted_requests = []
    current_table_index = 0
    remaining_amount = dp[n]
    for i in range(n, 0, -1):
        if remaining_amount <= 0:
            break
        group_size, group_spend = map(int, input().split())
        table_capacity = table_capacities[current_table_index]
        if table_capacity >= group_size and group_spend + dp[i - 1] > remaining_amount:
            accepted_requests.append((i, current_table_index))
            remaining_amount -= (group_spend + dp[i - 1])
            current_table_index = (current_table_index + 1) % k
        else:
            current_table_index = (current_table_index + 1) % k
    
    print(f"{len(accepted_requests)} {remaining_amount}")
    for i, j in accepted_requests:
        print(i, j)

solve()
