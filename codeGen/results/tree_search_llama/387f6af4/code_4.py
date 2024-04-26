import sys

def find_complement(N):
    # Calculate the maximum possible value for an integer (2^32 - 1)
    max_value = 2**31 - 1
    
    # Subtract N from the maximum possible value to get the complement
    return max_value - N

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(find_complement(N))
