from collections import deque

def minChanges(s, k):
    n = len(s)
    dp = [[0] * 3 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if s[i - 1] == 'R':
            expected = 0
        elif s[i - 1] == 'G':
            expected = 1
        else:
            expected = 2
        
        for c in range(3):
            if c != expected and dp[i - 1][c]:
                dp[i][expected] = min(dp[i][expected], dp[i - 1][c] + 1)
    
    return min(dp[n])

def main():
    n = int(input())
    k = int(input())
    s = input()
    
    print(minChanges(s, k))

if __name__ == "__main__":
    main()
