import sys

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        dp = [[[False] * (k + 1) for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][0] = True
        
        for i, (u, v) in enumerate(edges):
            for j in range(min(i + 1, k), -1, -1):
                for xor_val in range(2**30):
                    if (a[u - 1] ^ xor_val) % 2 == 0 and dp[u - 1][j][xor_val]:
                        dp[v - 1][k - i - 1][xor_val] = True
        
        print('YES' if dp[-1][-1][0] else 'NO')

if __name__ == '__main__':
    main()
