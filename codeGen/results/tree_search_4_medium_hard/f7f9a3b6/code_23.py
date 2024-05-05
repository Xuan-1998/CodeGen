def split_message(s, a):
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(26)]
    
    max_len = 0
    min_substr = float('inf')
    
    for i in range(n):
        for j in range(i+1, n+1):
            if all(c <= a[ord(s[i:j].lower()) - ord('a')] for c in s[i:j]):
                dp[ord(s[i-1].lower()) - ord('a')][j] = 1
                max_len = max(max_len, j - i)
    
    total_ways = sum(dp[-1])
    min_substr = min(min_substr, n // total_ways)
    
    print(total_ways % MOD)
    print(max_len)
    print(min_substr)

if __name__ == "__main__":
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    split_message(s, a)
