def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Input n and m
        dp = [[0] * (m + 1) for _ in range(len(str(n)) + 1)]
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, len(str(n)) + 1):
            for j in range(min(i, m) + 1):
                if j == 0:
                    dp[i][j] = i
                else:
                    last_digit = int(str(n)[i - 1])
                    new_value = (last_digit + 1) * (10 ** (i - 1))
                    length = i
                    for k in range(i):
                        if str(new_value)[k].isdigit():
                            length += 1
                    dp[i][j] = min(dp[i - 1][j - 1], j, length)
        print(dp[-1][-1] % (10**9 + 7))  # Print the result

solve()
