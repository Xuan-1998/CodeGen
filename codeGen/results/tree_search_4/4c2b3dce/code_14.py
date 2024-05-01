import sys

def solve():
    s = input()
    count_A = 0
    count_B = 0
    for c in s:
        if c == 'A':
            count_A += 1
        elif c == 'B':
            count_B += 1
    if (count_A > 0 and count_B > 0) or (count_A > 1 and count_B == 0) or (count_A == 0 and count_B > 1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
