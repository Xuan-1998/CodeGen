import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    max_or_value = 0
    for i in range(n):
        for j in range(i+1, n):
            or_val = int(s[:i+1], 2) | int(s[i:], 2)
            if or_val > max_or_value:
                max_or_value = or_val

    print(bin(max_or_value)[2:])

if __name__ == "__main__":
    solve()
