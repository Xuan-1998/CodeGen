import sys

def solve():
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    if k >= n:
        result = s * (k // n)
        remaining_chars = k % n
        if remaining_chars > 0 and s[remaining_chars - 1] <= s[0]:
            result += s[:remaining_chars]
        else:
            result += s
    else:
        if k == 1:
            return s[:-1]

        if s[k-1] <= s[0]:
            result = s[:-1]
        else:
            result = s

    print(result)

if __name__ == "__main__":
    solve()
