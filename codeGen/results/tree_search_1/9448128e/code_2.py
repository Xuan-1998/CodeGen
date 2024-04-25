MOD = 998244353

def count_sequences(sets):
    N = len(sets)
    dp = [{} for _ in range(N)]
    
    # Initialize the base case for the first set
    for x in sets[0]:
        dp[0][x] = 1
    
    # Fill the dp table
    for i in range(1, N):
        for x in sets[i]:
            dp[i][x] = 0
            # Consider all elements from the previous set
            for y in sets[i-1]:
                if x != y:
                    dp[i][x] += dp[i-1][y]
                    dp[i][x] %= MOD
    
    # Sum all possible last elements of the sequence
    answer = sum(dp[-1].values()) % MOD
    return answer

def main():
    N = int(input())
    sets = []
    for _ in range(N):
        A = list(map(int, input().split()))[1:]
        sets.append(A)
    print(count_sequences(sets))

if __name__ == "__main__":
    main()
