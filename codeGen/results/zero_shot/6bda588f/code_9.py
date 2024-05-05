def min_function_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Special case when s = 0
        if s == 0:
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                dp[i] = dp[i - 1] + a[i - 1] ** 2
            print(min(dp))
        
        # General case when s > 0
        else:
            ans = float('inf')
            for x in range((s + 1) // 2, min(s, sum(a)) // 2 + 1):
                F = 0
                y = 0
                for i in range(n):
                    a_i = a[i]
                    if a_i >= s:
                        x_i = (a_i - s) // 2
                        y_i = (a_i + s) // 2
                    else:
                        x_i = x
                        y_i = a_i - x
                    F += x_i * y_i
                    y += y_i
                ans = min(ans, F)
            print(ans)

if __name__ == '__main__':
    min_function_value()
