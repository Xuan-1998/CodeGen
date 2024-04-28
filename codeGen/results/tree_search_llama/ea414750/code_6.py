import sys

def solve():
    s = sys.stdin.readline().strip()
    bears = set()
    for i in range(len(s) - 3):
        if s[i:i+4] == 'bear':
            bears.add(i)
    
    count = 0
    for i in sorted(list(bears)):
        for j in range(i + 1, len(s) - 3):
            if s[j:j+4] == 'bear' and i <= j:
                count += 1
    
    print(count)

if __name__ == "__main__":
    solve()
