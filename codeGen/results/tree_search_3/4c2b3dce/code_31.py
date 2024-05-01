import sys

def solution():
    s = input().strip()
    seen_A = False
    for i, c in enumerate(s):
        if c == 'A':
            seen_A = True
        elif c == 'B' and seen_A:
            print("YES")
            return
    if not seen_A:
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'B':
                seen_B = True
            elif s[i] == 'A' and seen_B:
                print("YES")
                return
    print("NO")

solution()
