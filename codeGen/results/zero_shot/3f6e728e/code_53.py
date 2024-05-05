import sys

def main():
    T = int(input())
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_radii = list(map(int, input().split()))
        lower_radii = list(map(int, input().split()))

        dp = [0] * (C + 1)
        
        for i in range(1, C + 1):
            count_upper = sum(r <= i for r in upper_radii)
            count_lower = sum(r >= i - 1 for r in lower_radii)
            
            dp[i] = ((dp[i-1] if i > 0 else 1) * (count_upper * count_lower)) % (10**9 + 7)

        print(*dp, sep=' ')

if __name__ == "__main__":
    main()
