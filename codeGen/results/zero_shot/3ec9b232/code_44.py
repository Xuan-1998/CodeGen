import sys
from math import comb

def solve():
    n = int(sys.stdin.readline())
    M = list(map(int, sys.stdin.readline().split()))
    MOD = 10**9 + 7
    
    # Calculate all possible permutations
    perms = set()
    for i in range(1, n+1):
        curr_perm = [i]
        dfs(i, curr_perm, perms)
    
    # Count unique permutations that result in M when sorted
    res = 0
    for perm in perms:
        if sorted(perm) == M:
            res += 1
    
    print(res % MOD)

def dfs(num, curr_perm, perms):
    if len(curr_perm) == len(set(curr_perm)):
        perms.add(tuple(sorted(curr_perm)))
        return
    for i in range(len(curr_perm), -1, -1):
        dfs(num, curr_perm[:i] + [num], perms)
        num += 1

if __name__ == "__main__":
    solve()
