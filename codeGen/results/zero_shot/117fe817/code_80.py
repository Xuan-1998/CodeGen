import sys

def count_digit_ones(n):
    return (n + 1) * (n // 2) + 1

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(count_digit_ones(n))
