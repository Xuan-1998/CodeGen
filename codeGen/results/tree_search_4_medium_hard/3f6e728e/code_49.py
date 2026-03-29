import sys; input = sys.stdin.readline
from collections import defaultdict

def read_input():
    T = int(input())
    result = []
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        result.append((N, M, C, U, L))
    return result

def solve(N, M, C, U, L):
    MOD = 10**9 + 7
    dp = defaultdict(int)
    for i in range(C+1):
        if i == 0:
            dp[i] = 1
        else:
            for j in range(min(i, N), -1, -1):
                if U[j-1] >= i:
                    break
            for k in range(min(i, M), -1, -1):
                if L[k-1] >= i:
                    break
            dp[i] = (dp[i-1] * comb(N-j+M-i, M-k) + sum(dp[j] * comb(N-j+M-i-j, M-k-j) for j in range(i))) % MOD
    return [str(dp[i]) for i in range(C+1)]

def main():
    inputs = read_input()
    outputs = []
    for N, M, C, U, L in inputs:
        outputs.append(solve(N, M, C, U, L))
    print(*[' '.join(output) for output in outputs], sep='\n')

if __name__ == "__main__":
    main()
