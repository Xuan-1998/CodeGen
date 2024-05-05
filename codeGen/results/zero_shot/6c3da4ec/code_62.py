import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    max_or = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate bitwise OR value for substrings [i:j+1] and [j:i]
            or_val1 = int(s[i:j+1], 2)
            or_val2 = int(s[j:i], 2)
            or_val = or_val1 | or_val2
            max_or = max(max_or, or_val)

    print(bin(max_or)[2:].zfill(n).lstrip('0') or '0')

if __name__ == '__main__':
    solve()
