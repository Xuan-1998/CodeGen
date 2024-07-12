python
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    # There are always 2 valid matrices: all zeros and all ones
    result = 2 % 998244353
    
    print(result)

if __name__ == "__main__":
    main()

