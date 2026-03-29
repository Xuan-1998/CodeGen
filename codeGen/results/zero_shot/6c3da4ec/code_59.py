import sys

def solve():
    n = int(input())
    s = input()

    max_or_value = 0
    for i in range(n):
        for j in range(i+1, n):
            left_substr = s[:i]
            right_substr = s[i:j+1]

            left_int_val = int(left_substr, 2)
            right_int_val = int(right_substr, 2)

            or_value = left_int_val | right_int_val
            max_or_value = max(max_or_value, or_value)

    print(bin(max_or_value)[2:].zfill(n).lstrip('0') or '0')

if __name__ == "__main__":
    solve()
