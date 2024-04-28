from collections import defaultdict

def common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    seen = set()
    
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if str1[i:j+1] == str2[j:i-1:-1]:
                dp[i][j] = (dp[i][j] or 1) and len(seen)
                seen.add(str1[i:j+1])
    
    return max(max(row) for row in dp) - min(min(col) for col in zip(*dp))

if __name__ == "__main__":
    str1, str2 = input().split()
    print(common_substrings(str1, str2))
