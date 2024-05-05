import sys

def solve():
    dp = {}
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        expected_color = s[k-1]
        ans = 0
        for i in range(k):
            if s[i] != expected_color:
                ans += 1
        print(ans)

if __name__ == "__main__":
    solve()
