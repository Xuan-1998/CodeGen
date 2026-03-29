import sys

def solve():
    n, k, max_group_size = map(int, input().split())
    dp = [[0] * (max_group_size + 1) for _ in range(k + 1)]
    
    # Initialize the base case: no requests
    for i in range(1, max_group_size + 1):
        dp[0][i] = 0
    
    for request in range(n):
        group_size, total_spending = map(int, input().split())
        
        for tables in range(k + 1):
            # If the current request can be seated
            if group_size <= tables:
                # Calculate the maximum amount of money earned
                max_earn = max(dp[tables - 1][group_size], total_spending)
                
                # Update the dynamic programming table
                dp[tables][group_size] = max(dp[tables][group_size], max_earn)
            else:
                # If the current request cannot be seated, decline it
                dp[tables][group_size] = dp[tables][group_size - 1]
        
        # Find the maximum amount of money earned and the minimum number of tables required
        max_earn = max(dp[-1])
        min_tables = dp[-1].index(max_earn) + 1
        
        print(*[max_earn, min_tables], sep='\n')

    for i in range(n):
        request_number, table_number = map(int, input().split())
        
        if dp[table_number][request_number] == request_number:
            print(*[i + 1, table_number], sep=' ')

if __name__ == "__main__":
    solve()
