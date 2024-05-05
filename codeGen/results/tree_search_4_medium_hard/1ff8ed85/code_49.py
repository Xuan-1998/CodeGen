def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [False] * (n + 1)
        dp[0] = True
        even_count = 0
        odd_count = 0
        for i in range(n):
            if b[i] % 2 == 0:
                even_count += 1
                if odd_count > 0 and dp[i - odd_count]:
                    dp[i + 1] = True
                elif even_count > 0 and dp[i - even_count]:
                    dp[i + 1] = True
            else:
                odd_count += 1
                if even_count > 0 and dp[i - even_count]:
                    dp[i + 1] = True
                elif odd_count > 0 and dp[i - odd_count]:
                    dp[i + 1] = True
        print("YES" if dp[n] else "NO")

can_send_over_network()
