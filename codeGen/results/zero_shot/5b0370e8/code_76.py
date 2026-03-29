import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 2**k - 1
        xor_result = sum(1 << (i % k) for i in range(n))
        count = 0
        for i in range(n):
            if ((and_result >> i) & 1) == ((xor_result >> i) & 1):
                count += 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
