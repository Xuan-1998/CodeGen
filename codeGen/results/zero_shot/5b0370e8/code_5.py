import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = 1 if all(2^k - 1 >= x for x in input().split()) else 0
        xor_count = sum(bin(x).count('1') for x in input().split())
        print((and_count + sum(bin(x).count('1') for x in input().split())) % (10**9 + 7))

if __name__ == '__main__':
    solve()
