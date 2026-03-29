import sys

def solve():
    n = int(sys.stdin.readline())
    mod = 998244353
    total_configurations = 2**n
    invalid_configurations = (n+1)*(n**2)
    valid_configurations = total_configurations - invalid_configurations
    probability = pow(2, n, mod) * pow(total_configurations, mod-2, mod) * pow(valid_configurations, mod-2, mod) * pow(invalid_configurations, mod-2, mod), -1, mod)
    print(probability)

if __name__ == "__main__":
    solve()
