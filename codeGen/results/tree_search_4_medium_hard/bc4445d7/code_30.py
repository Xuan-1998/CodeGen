from collections import defaultdict

def solve(n, edges, k):
    dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n-1)]
    
    memo = defaultdict(int)
    
    for i in range(1, n):
        for j in range(i+1, n):
            if (i,j) in edges:
                for label in range(1,k+1):
                    dp[i][j][label] = max(dp[i][j][label], 
                                            memo.get((i-1,label),0) + f(i,j)*label)
                    
    return sum(sum(row) for row in dp[0])

def f(u,v,k):
    # implement your logic to calculate the sum f(u,v) given k and edge labels
    pass

# Example usage:
n = int(input())
edges = [(int(x)-1,int(y)-1) for x,y in [input().split() for _ in range(n-1)]]
k = int(input())

print(solve(n, edges, k))
