MOD = 998244353

def main():
    N = int(input().strip())  # Number of sets
    dp = []  # dp[i][j] - number of valid sequences ending with j using first i sets
    sum_dp = [1]  # sum_dp[i] - sum of all dp[i][j] for a given i

    for _ in range(N):
        # Read the current set
        _, *current_set = map(int, input().split())
        new_dp = {}
        new_sum = 0

        for element in current_set:
            # Compute the number of sequences that can end with this element
            if element in dp:
                new_dp[element] = (sum_dp[-1] - dp[element]) % MOD
            else:
                new_dp[element] = sum_dp[-1] % MOD
            new_sum = (new_sum + new_dp[element]) % MOD

        # Update the states
        dp = new_dp
        sum_dp.append(new_sum)

    # The answer is the sum of dp values for the last set
    print(sum_dp[-1])

if __name__ == "__main__":
    main()
