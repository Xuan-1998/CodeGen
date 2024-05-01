import sys

def solve():
    s = sys.stdin.readline().strip()
    if 'AB' in s:
        s = s.replace('AB', '', 1)
        if 'BA' in s:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
