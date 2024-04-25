MOD = 998244353

def main():
    N = int(input().strip())
    sets = [list(map(int, input().split()))[1:] for _ in range(N)]
    
    # Initialize the dp array with the first set
    dp_prev = {x: 1 for x in sets[0]}
    
    for i in range(1, N):
        dp_curr = {}
        sum_prev = sum(dp_prev.values()) % MOD
        
        for num in sets[i]:
            # If the number is in the previous set, we subtract the count of sequences
            # ending with that number to avoid repetition.
            dp_curr[num] = (sum_prev - dp_prev.get(num, 0)) % MOD
        
        dp_prev = dp_curr
    
    # The answer is the sum of the counts of sequences ending with each number in the last set
    result = sum(dp_prev.values()) % MOD
    print(result)

if __name__ == "__main__":
    main()
