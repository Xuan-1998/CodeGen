MOD = 998244353

def count_common_elements(set1, set2):
    return len(set1 & set2)

def main():
    # Read the number of sets
    N = int(input().strip())
    
    # Read the sets
    sets = []
    for _ in range(N):
        line = list(map(int, input().split()))
        sets.append(set(line[1:]))  # Convert list to set to remove duplicates
    
    # Initialize dp array
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = len(sets[0])
    dp[0][1] = 0  # There is no previous set to compare with the first set
    
    # Fill the dp array
    for i in range(1, N):
        common_elements = count_common_elements(sets[i], sets[i-1])
        dp[i][0] = (dp[i-1][1] * (len(sets[i]) - common_elements)) % MOD
        dp[i][1] = (dp[i-1][0] * common_elements) % MOD
    
    # The answer is the sum of the two possibilities for the last set
    answer = (dp[N-1][0] + dp[N-1][1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
