import sys

def max_bitwise_or(s):
    n = len(s)
    # Calculate the maximum possible value by choosing the longest substrings
    max_val = int('1' * (n // 2), 2) if n % 2 == 0 else int('1' * ((n + 1) // 2), 2)
    return bin(max_val)[2:]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(max_bitwise_or(s))
