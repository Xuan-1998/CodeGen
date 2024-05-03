from math import comb

def prob(n, probs):
    dp = [[[0.0 for _ in range(2**n)] for _ in range(comb(2, r))] for r in range(n+1)]
    
    # Base case: when there's only one possible combination left (i.e., n=1)
    if n == 1:
        return probs[0][0] + probs[0][1]

    # Fill up the table by iterating through each ticket, considering all previous combinations
    for r in range(2):
        for prev_combination in range(comb(2, r)):
            total_prob = 0.0
            new_number = (prev_combination >> r) & 1
            new_number_prob = probs[r][new_number]
            
            # Calculate the probability of correct numbering given the previous tickets
            if r > 0:
                for prev_ticket in range(n):
                    if not ((prev_combination >> prev_ticket) & 1):
                        total_prob += dp[r-1][prev_combination^(1<<prev_ticket)][new_number]
            
            # Update the probability of correct numbering
            total_prob *= new_number_prob
            
            # Store the updated value in the table
            for combination in range(comb(2, n-r)):
                dp[n][combination][new_number] = total_prob
                
    # Return the final answer
    return sum([dp[n][-1][i] for i in range(2**n)])
