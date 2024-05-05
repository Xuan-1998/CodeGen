code = '''
n_cases = int(input())
for _ in range(n_cases):
    n = int(input())
    b = list(map(int, input().split()))
    dp = [0] * (n + 1)
    prev_val = None
    for i in range(1, n + 1):
        for j in range(i):
            if b[j] == prev_val:
                len_ = i - j
                break
        dp[i] = max(dp[i-1], len_ + b[j])
        prev_val = b[j]
    print("YES" if dp[n] > 0 else "NO")
'''

print(code)
