import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    # Calculate prefix sums
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        if s[i] == '1':
            prefix_sums[i + 1] = prefix_sums[i] + 1
        else:
            prefix_sums[i + 1] = prefix_sums[i]

    max_or = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            or_val = prefix_sums[j] ^ (prefix_sums[i] | ~prefix_sums[i])
            max_or = max(max_or, or_val)

    print(bin(max_or)[2:].zfill(n))

if __name__ == '__main__':
    solve()
