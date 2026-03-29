def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = {(i, prev): False for i, (prev,) in enumerate(b)}
        
        dp[0] = True
        
        for i, val in enumerate(b):
            if dp[i-1]:
                dp[(i, val)] = True
            else:
                dp[(i, val)] = False
                
        print('YES' if any(val for _, val in dp.values()) else 'NO')

if __name__ == "__main__":
    main()
