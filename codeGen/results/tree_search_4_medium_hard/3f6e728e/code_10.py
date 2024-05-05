import sys
input = sys.stdin.readline

def main():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        dp = [0] * (C + 1)
        dp[0] = 1
        
        for i in range(C):
            for j in range(1, i + 2):
                if U.count(j) > 0 and L.count(i - j + 1) > 0:
                    dp[i] += dp[j - 1]
                    dp[i] %= MOD
        
        print(*dp)

if __name__ == "__main__":
    main()
