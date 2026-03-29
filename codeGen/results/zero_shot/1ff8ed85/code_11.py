def send_sequence_over_network():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # size of the sequence b
        b = list(map(int, input().split()))  # sequence b

        dp = [False] * (n + 1)  # dynamic programming table
        dp[0] = True  # base case: empty prefix is always possible

        for i in range(n):
            for j in range(i + 1, n):
                if abs(b[i] - b[j]) <= j - i:
                    dp[j] = dp[i] or dp[j]
                else:
                    break
            if not dp[j]:
                break

        print("YES" if dp[-1] else "NO")
