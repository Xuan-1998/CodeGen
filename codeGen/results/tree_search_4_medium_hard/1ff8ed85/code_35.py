def send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        # Initialize the state dictionary and cumulative sum list
        state = {}
        cum_sum = [0]
        curr_sum = 0
        
        # Calculate the frequency count of each value in sequence a
        for x in range(1, max(b) + 2):
            if x not in b:
                state[x] = 0
            else:
                state[x] = state.get(x, 0) + 1
                
        # Construct the cumulative sum list and update it as you iterate through sequence b
        for x in b:
            curr_sum += x
            cum_sum.append(curr_sum)
            
        # Initialize the table with the minimum number of segments needed to form each prefix of sequence b
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Fill up the table using dynamic programming
        for i in range(1, n):
            if cum_sum[i] >= b[i]:
                dp[i] = min(dp[i-1], state.get(b[i]-cum_sum[i-1], float('inf')) + 1)
            else:
                dp[i] = min(dp[i-1], dp[i-1] + 1)
                
        # Print the minimum number of segments needed to form sequence b
        if dp[-1] == float('inf'):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    send_over_network()
