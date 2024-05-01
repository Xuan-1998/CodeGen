import sys

def solve():
    s = input().strip()
    state = 0
    ab_substrings = set()
    ba_substrings = set()

    for i in range(len(s)):
        if s[i] == 'A':
            state ^= 1
            if i >= 2 and s[i-1:i+1] == 'AB' and s[:i] not in ab_substrings:
                ab_substrings.add(s[:i])
            if i >= 2 and s[i-1::-1] == 'BA' and s[:i][::-1] not in ba_substrings:
                ba_substrings.add(s[:i][::-1])
        else:
            state ^= 1
            if i >= 2 and s[i-1:i+1] == 'BA' and s[:i] not in ba_substrings:
                ba_substrings.add(s[:i])
            if i >= 2 and s[i-1::-1] == 'AB' and s[:i][::-1] not in ab_substrings:
                ab_substrings.add(s[:i][::-1])

    if 'AB' in ab_substrings or 'BA' in ba_substrings:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
