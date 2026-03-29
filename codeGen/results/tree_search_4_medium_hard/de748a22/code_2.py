from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    # Calculate prefix sum array for sign-variable sums
    var_sum = 0
    var_sums = [0]
    for sign in signs:
        if sign == "+":
            var_sum += 1
        else:
            var_sum -= 1
        var_sums.append(var_sum)

    # Initialize DP table
    dp = defaultdict(int)
    memo = {}

    def dp_query(l, r):
        if (l, r) in memo:
            return memo[(l, r)]
        
        min_remove = float('inf')
        for i in range(l, r+1):
            pos_sum = sum(var_sums[i:])  # sum of positive signs from l to r
            neg_sum = -sum(var_sums[:i])  # sum of negative signs up to i
            
            if (pos_sum >= 0 and neg_sum <= 0) or (pos_sum <= 0 and neg_sum >= 0):
                min_remove = min(min_remove, dp_query(i, r) + 1)
        
        memo[(l, r)] = min_remove
        return min_remove
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(dp_query(l-1, r))

if __name__ == "__main__":
    solve()
