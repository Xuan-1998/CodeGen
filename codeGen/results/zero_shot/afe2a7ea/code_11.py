import math
MOD = 998244353

def solve(n):
    # Calculate the probability that there will be a way to set signal powers so that all constraints are met
    probability = 1
    for i in range(1, n+1):
        # For each town, calculate the number of ways to assign a tower to it without considering previous towns
        num_ways = math.comb(n-i+1, i)
        
        # Update the total probability
        probability *= (num_ways * 2**(n-i)) % MOD

    return probability

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
