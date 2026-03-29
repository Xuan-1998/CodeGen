import sys

def solve():
    n = int(input())
    s = input()

    dp_pre = {0: 0}
    max_or_value = 0

    for i in range(1, n):
        or_val = dp_pre[i-1]
        if s[i] == '1':
            or_val |= (1 << i)
        dp_pre[i] = or_val
        max_or_value = max(max_or_value, dp_pre[i])

    return bin(max_or_value)[2:]

if __name__ == '__main__':
    print(solve())
