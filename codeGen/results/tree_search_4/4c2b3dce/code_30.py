import sys

def solve():
    s = input()
    found_AB = False
    for i in range(len(s)):
        if s[i:i+2] == "AB":
            found_AB = True
        elif s[i:i+2] == "BA" and found_AB:
            print("YES")
            return
    if found_AB:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
