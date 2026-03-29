import sys

def min_changes(s, k):
    n = len(s)
    res = 0
    for i in range(n - k + 1):
        substr = s[i:i+k]
        if not any(c in "RGB" for c in substr):
            res += k
        else:
            for j in range(k):
                if substr[j] == 'R' and s[i+j].lower() != 'r':
                    res += 1
                elif substr[j] == 'G' and s[i+j].lower() != 'g':
                    res += 1
                elif substr[j] == 'B' and s[i+j].lower() != 'b':
                    res += 1
    return res

q = int(sys.stdin.readline())
for _ in range(q):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
