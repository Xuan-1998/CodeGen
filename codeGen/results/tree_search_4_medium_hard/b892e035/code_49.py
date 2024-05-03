import sys

def calculate_probability():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        probs = []
        
        # Read probabilities and numbers from stdin
        for _ in range(n):
            prob1, num1, num2 = map(float, input().split())
            probs.append((prob1, num1, num2))
        
        # Initialize the DP table
        dp = [[0.0] * 17 for _ in range(51)]
        
        # Base cases: if only one possible number or no more tickets left, probability is either 1 (correct) or 0 (incorrect)
        for i in range(n):
            dp[i][num1] = probs[i][0]
            dp[i][num2] = 1 - probs[i][0]
        
        # Fill in the DP table using the transition relationship
        for i in range(1, n):
            for j in range(17):
                if dp[i-1][j] > 0:
                    dp[i][j] = (probs[i][0] * dp[i-1][min(num1, num2)] + 
                                (1-probs[i][0]) * dp[i-1][max(num1, num2)]) / probs[i][0]
        
        # Calculate the total probability
        total_prob = sum(dp[-1])
        
        # Round the result to 6 decimal places and print it to stdout
        print('%.6f' % total_prob)

if __name__ == '__main__':
    calculate_probability()
