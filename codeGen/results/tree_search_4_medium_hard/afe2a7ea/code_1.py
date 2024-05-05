def solve():
    n = int(input())
    memo = {(0, 0): True}

    def dp(i, k):
        if (i, k) not in memo:
            if i == 0 or k > 0:
                if i % 2 == 0 and k == 0 or i % 2 != 0 and dp(i - 1, k - 1):
                    memo[(i, k)] = True
                else:
                    memo[(i, k)] = False
            else:
                memo[(i, k)] = False
        return memo[(i, k)]

    ans = sum(int(dp(i, 0)) for i in range(n + 1))
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
