import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    # Counting the number of substrings
    r_count, g_count, b_count = 0, 0, 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        elif s[i] == 'G':
            g_count += 1
        else:
            b_count += 1

    # Finding the minimum number of changes
    max_diff = max(r_count, g_count, b_count) - min(r_count, g_count, b_count)
    print(max_diff)

for _ in range(int(input())):
    solve()
