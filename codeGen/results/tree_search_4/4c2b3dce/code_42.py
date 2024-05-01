import sys

def solve():
    s = sys.stdin.readline().strip()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == 'A' and s[j] == 'B':
            if s[i+1:j].find('AB') != -1 and s[:i].find('BA') != -1:
                print("YES")
                return
        elif s[i] == 'B' and s[j] == 'A':
            if s[i+1:j].find('BA') != -1 and s[:i].find('AB') != -1:
                print("YES")
                return
        i += 1
        j -= 1
    print("NO")

if __name__ == "__main__":
    solve()
