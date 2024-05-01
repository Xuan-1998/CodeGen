import sys

def solve():
    s = input().strip()
    if len(s) < 2:
        print("NO")
        return
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB":
            if s[i+2:] == s[:i].[::-1]:
                print("YES")
                sys.exit()
    print("NO")

if __name__ == "__main__":
    solve()
