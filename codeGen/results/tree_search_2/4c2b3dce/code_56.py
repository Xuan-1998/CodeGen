from collections import Counter

def solve():
    s = input()
    a_count = Counter(s)['A']
    b_count = Counter(s)['B']

    if (a_count > 0 and b_count == 0) or (b_count > 0 and a_count == 0):
        print("NO")
    else:
        for i in range(len(s)):
            if s[i:i+2] in ["AB", "BA"]:
                print("YES")
                return
        print("NO")

if __name__ == "__main__":
    solve()
