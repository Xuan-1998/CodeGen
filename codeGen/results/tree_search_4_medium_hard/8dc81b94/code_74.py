import sys

def process_array(a):
    dp = [False] * (len(a) + 1)
    dp[0] = True

    for i in range(len(a)):
        if a[i] > 0:
            dp[i+1] = False
        else:
            dp[i+1] = dp[i]

    return "YES" if dp[-1] else "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(process_array(a))
