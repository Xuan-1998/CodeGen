from sys import stdin

def solve():
    N, K = map(int, stdin.readline().split())
    Arr = list(map(int, stdin.readline().split()))
    
    dp = [0] * N
    for i in range(N):
        max_val = max(Arr[i:])
        if max_val > K:
            dp[i] = i + 1
        else:
            j = i - 1
            while j >= 0 and max(Arr[j:i+1]) <= K:
                j -= 1
            if j >= 0:
                dp[i] = i - j
    
    print(sum(1 for x in dp if x > 0))

solve()
