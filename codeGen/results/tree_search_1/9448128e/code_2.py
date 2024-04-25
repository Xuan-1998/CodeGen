MOD = 998244353

def main():
    N = int(input().strip())
    sets = [list(map(int, input().strip().split()))[1:] for _ in range(N)]

    # Initialize dp with zeros
    dp = [{x: 0 for x in sets[i]} for i in range(N)]
    
    # Initialize the first set's dp values
    for x in sets[0]:
        dp[0][x] = 1

    # Fill the dp table
    for i in range(1, N):
        # Calculate the total sum of the previous set's dp values
        total_sum = sum(dp[i-1].values()) % MOD
        
        for x in sets[i]:
            # If x is in the previous set, subtract its dp value from the total sum
            dp[i][x] = (total_sum - dp[i-1].get(x, 0)) % MOD

    # The answer is the sum of dp values of the last set
    answer = sum(dp[-1].values()) % MOD
    print(answer)

if __name__ == "__main__":
    main()
