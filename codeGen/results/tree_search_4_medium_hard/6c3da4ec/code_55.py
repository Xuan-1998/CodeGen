import sys

def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(n):
        dp[i+1] = s[i]
        
        for j in range(i, -1, -1):
            if not dp[j]:
                break
            dp[i+1] = max(dp[i+1], dp[j]|int(s[i]))
    
    return bin(max([bin(int(x, 2)) for x in dp[1:]])).replace("0b", "")

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(max_bitwise_or(s))
