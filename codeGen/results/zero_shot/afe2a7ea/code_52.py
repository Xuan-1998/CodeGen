import sys

def solve(n):
    MOD = 998244353
    total_configurations = 1 << n
    valid_configurations = 0
    
    for i in range(2**n):
        config = bin(i)[2:].zfill(n)
        
        # Check constraints
        if (config[0] == '0' and config[n-1] == '0'):
            valid_towns = sum([int(x) for x in config[1:n]])
            
            # Towns 1 to n get signal from exactly one tower each
            if valid_towns == 1:
                valid_configurations += 1
    
    return (valid_configurations * pow(2, n, MOD)) % MOD

n = int(sys.stdin.readline())
print(solve(n))
