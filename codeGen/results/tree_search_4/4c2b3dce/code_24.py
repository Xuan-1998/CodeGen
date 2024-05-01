def solve(s):
    n = len(s)

    def helper(left, right):
        if left >= right:
            return False

        for i in range(min(left + 1, right - 1)):
            if s[left:i] == "AB" and s[i:right] == "BA":
                return True
        return False

    for i in range(n // 2):
        if helper(i, n - i - 1):
            return "YES"
    return "NO"


import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(solve(s))
