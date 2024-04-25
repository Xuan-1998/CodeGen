MOD = 998244353

def main():
    N = int(input().strip())
    sets = [list(map(int, input().split()))[1:] for _ in range(N)]

    # Initialize dp with the first set, since any element can be the last element
    dp = {x: 1 for x in sets[0]}

    # Iterate over the sets
    for s in range(1, N):
        next_dp = {}
        # Get the sum of the previous states
        total = sum(dp.values()) % MOD
        for x in sets[s]:
            # Subtract the count of sequences ending with the same element to avoid repetition
            next_dp[x] = (total - dp.get(x, 0)) % MOD
        dp = next_dp

    # The answer is the sum of all possible sequences from the last set
    print(sum(dp.values()) % MOD)

if __name__ == "__main__":
    main()
