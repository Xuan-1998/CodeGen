python
MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    # The number of valid matrices is 2^(N + M - 1) modulo 998244353
    result = pow(2, N + M - 1, MOD)
    
    print(result)

if __name__ == "__main__":
    main()

