from collections import defaultdict

def check_string(s):
    even_count = 0
    odd_count = 0
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'A':
            even_count += 1
            odd_count = 0
        else:
            even_count = 0
            odd_count += 1
        
        if (i % 2 == 0 and even_count > 0 and odd_count < 1) or (i % 2 != 0 and even_count < 1 and odd_count > 0):
            dp[i] = True
    
    return "YES" if dp[-1] else "NO"

if __name__ == "__main__":
    s = input()
    print(check_string(s))
