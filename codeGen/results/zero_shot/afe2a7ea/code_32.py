import math

def solve():
    n = int(input())
    
    # Calculate the number of valid configurations
    total_configs = 2 ** n  # 2^n because each tower has a choice of 2 signal powers (1 to n)
    
    # Subtract invalid configurations
    invalid_configs = math.comb(n + 1, n)  # calculate the number of ways towns 0 and n+1 can get signal from same towers
    valid_configs = total_configs - invalid_configs
    
    # Calculate the probability modulo 998244353
    prob = pow(2, n, 998244353)
    
    print((valid_configs * prob) % 998244353)

if __name__ == "__main__":
    solve()
