import sys

def solve(n):
    MOD = int(1e9) + 7
    dp = [0] * (n + 1)
    for i in range(10**n, -1, -1):
        s = str(i).zfill(n)
        cur_len = 0
        for j in range(n):
            if s[j] == s[0]:
                cur_len += 1
            else:
                break
        dp[cur_len] += 1
    return ' '.join(map(str, [x % MOD for x in dp]))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solve(n))
