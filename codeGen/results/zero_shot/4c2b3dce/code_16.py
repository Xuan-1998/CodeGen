import sys

def solve():
    s = sys.stdin.readline().strip()
    if "AB" in s and "BA" not in s[:s.index("AB")]:
        print("YES")
    elif "BA" in s and "AB" not in s[s.index("BA"):]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
