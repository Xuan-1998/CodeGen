import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (2**k)
        xnor_count = [0] * (2**k)
        for num in map(int, input().split()):
            bit = 1
            for i in range(k-1, -1, -1):
                if ((num >> i) & 1) == 1:
                    and_count[bit] += 1
                    xnor_count[bit] += (num >> i) & 1
                    bit <<= 1
        ans = 0
        for i in range(2**k):
            if and_count[i] > xnor_count[i]:
                ans = (ans + and_count[i]) % (10**9+7)
        print(ans)

if __name__ == "__main__":
    solve()
