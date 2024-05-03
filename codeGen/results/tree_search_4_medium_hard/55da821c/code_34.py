from sys import stdin

def dp(i, j):
    if i > 1:
        return min(dp(i-1, k) for k in range(j+1))
    else:
        return j

n, m = map(int, stdin.readline().split())
plants = [map(int, line.split()) for line in stdin.readlines()]

print(dp(m, n-1))
