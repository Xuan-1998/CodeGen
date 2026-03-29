import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        changes = 0
        for i in range(n - k + 1):
            window = s[i:i+k]
            if not all(c in 'RGB' for c in window):  # Check if the substring is present in the infinite string
                changes += len(set(window))  # Count the number of unique characters that need to be changed
        print(changes)

if __name__ == '__main__':
    solve()
