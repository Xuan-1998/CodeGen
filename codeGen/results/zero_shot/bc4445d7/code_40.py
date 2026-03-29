import sys
input = sys.stdin.readline

def read_input():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    m = int(input())
    primes = list(map(int, input().split()))
    return n, edges, m, primes

def solve(n, edges, m, primes):
    # Calculate the minimum possible sum of numbers on edges
    min_sum = 1
    for prime in primes:
        min_sum *= prime
    
    # Initialize dp array with -1
    dp = [-1] * (n+1)
    
    # Fill up the dp array
    for u, v in edges:
        if dp[u] == -1:
            dp[u] = 0
        if dp[v] == -1:
            dp[v] = 0
        if dp[u] + 1 != dp[v]:
            continue
        min_sum //= (dp[u]+1)
        dp[u+1:] = [i for i in dp[u+1:] if (min_sum**(i-dp[u])) % (10**9 + 7) == 0]
    
    # Calculate the maximum possible distribution index
    max_distribution_index = sum((dp[i]-1)*(n-i-1) for i in range(1, n))
    
    return str(max_distribution_index % (10**9+7))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, edges, m, primes = read_input()
        print(solve(n, edges, m, primes))
