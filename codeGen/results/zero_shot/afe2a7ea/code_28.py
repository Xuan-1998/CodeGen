import sys

def solve():
    n = int(sys.stdin.readline())
    
    # Calculate the total number of possible configurations
    total_configurations = 1
    for _ in range(n):
        total_configurations *= (n - _)
    total_configurations %= 998244353
    
    # Count valid configurations
    valid_configurations = 0
    for config in range(total_configurations):
        is_valid = True
        tower_signals = [0] * n
        for signal in range(1, n + 1):
            if (config >> (signal - 1)) & 1:
                for _ in range(signal - 1):
                    if not (tower_signals[_]):
                        tower_signals[_] = signal
                        break
                    is_valid = False
                if not is_valid:
                    break
        if is_valid:
            valid_configurations += 1
    
    # Calculate the probability and print the result
    probability = valid_configurations * 2 ** n
    print(probability % 998244353)

if __name__ == "__main__":
    solve()
