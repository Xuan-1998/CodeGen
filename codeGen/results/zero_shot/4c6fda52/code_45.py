import sys

def solve(s, k):
    n = len(s)
    ans = 0
    for i in range(n - k + 1):
        window = s[i:i+k]
        if window.count('R') > window.count('G') or window.count('R') > window.count('B'):
            ans += (window.count('R') - min(window.count('G'), window.count('B')))
    return ans

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        print(solve(s, k))

if __name__ == "__main__":
    main()
