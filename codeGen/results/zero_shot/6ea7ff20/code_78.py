import sys

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    
    p.sort()
    
    for i in range(len(p)):
        if i % 2 == 0:
            left = []
            right = []
            for j in range(i//2):
                left.append(p[j])
                right.append(p[-1-j])
            if left + right != p[:i+1]:
                return "NO"
    return "YES"

print(solve())
