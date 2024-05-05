import sys

def read_input():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    return n, s

n, s = read_input()

# Initialize dp array with zeros
dp = [[False] * (n + 1) for _ in range(n + 1)]

