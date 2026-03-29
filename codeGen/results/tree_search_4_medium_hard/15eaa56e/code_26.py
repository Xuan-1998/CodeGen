def solve():
    n, m = map(int, input().split())
    dp = [[False] * (m+1) for _ in range(n+1)]
    
    # Calculate the next state based on the current state:
    for i in range(2, n+1):
        for c in range(m+1):
            if all(arr[j] <= arr[c] for j in range(c)):
                dp[i][c] = True
            else:
                dp[i][c] = False
    
    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        
        # Check if any column is sorted in non-decreasing order from row l to r
        for c in range(m+1):
            if all(dp[i][c] for i in range(l, r+1)):
                print("Yes")
                return
        
    print("No")

if __name__ == "__main__":
    solve()
