import sys

def solve(s):
    n = len(s)
    dp = [False] * (n + 1)

    def find_ab_ba(i):
        if i >= n or s[i:] not in ["AB", "BA"]:
            return False
        return True

    for i in range(n - 1, -1, -1):
        if find_ab_ba(i):
            dp[i] = True
            return "YES"

    return "NO"


def main():
    s = input().strip()
    print(solve(s))


if __name__ == "__main__":
    main()
