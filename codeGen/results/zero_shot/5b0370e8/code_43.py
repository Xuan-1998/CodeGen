import math

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        for _ in range(n):
            x = int(input())
            bits_set = bin(x).count('1')
            if bits_set >= k:
                count += 1
        print((math.pow(2, k-1) - 1)**(n-k+1) % (10**9 + 7))

if __name__ == "__main__":
    solve()
