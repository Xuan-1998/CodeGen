import sys

def has_ab_ba(s):
    if "AB" in s and "BA" not in s[:s.index("AB")]:
        return "YES"
    if "BA" in s and "AB" not in s[:s.index("BA")]:
        return "YES"
    return "NO"

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(has_ab_ba(s))
