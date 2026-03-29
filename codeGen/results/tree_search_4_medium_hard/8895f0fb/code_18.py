import sys

def main():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        # Initialize the DP table with zeros
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        # Fill up the DP table
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if (i >= 5 and j >= 5) or (i >= 5 and j < 5) or (i < 5 and j >= 5):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        
        # Calculate the expected number of non-zero carries
        total_pairs = N * N
        non_zero_carries = sum([sum(row) for row in dp])
        
        print(non_zero_carries / total_pairs)

if __name__ == "__main__":
    main()
