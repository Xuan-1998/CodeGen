def solve():
    t = int(input())  # read the number of test cases

    for _ in range(t):
        n = int(input())  # read the length of sequence b
        b = list(map(int, input().split()))  # read sequence b itself

        dp = [False] * (n + 1)  # initialize dynamic programming state
        prev_val = None  # keep track of previous value in sequence b

        for i in range(n):
            if prev_val is not None and abs(b[i] - prev_val) == 1:
                dp[i + 1] = True
            prev_val = b[i]

        print('YES' if dp[-1] else 'NO')  # output the result

if __name__ == '__main__':
    solve()
