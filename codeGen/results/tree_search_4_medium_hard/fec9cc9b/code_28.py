n, m = map(int, input().split())
arr = list(map(int, input().split()))
seen = [0] * (n + 1)

dp = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    seen[i] = i
    while seen[i] > 0 and arr[seen[i] - 1] < arr[i]:
        seen[i] -= 1

for l in range(1, n + 1):
    for r in range(l, n + 1):
        if arr[r] > arr[l - 1]:
            inc = 0
            dec = 0
            flag = True
            for i in range(l, r + 1):
                if arr[i] > arr[i - 1]:
                    inc += 1
                    dec = 0
                elif arr[i] < arr[i - 1]:
                    dec += 1
                    inc = 0
                else:
                    flag = False
                    break
            dp[l][r] = flag

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] else "No")
