import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())
        and_result = 2**k - 1
        xor_result = 0
        count = 0
        for num in map(int, sys.stdin.readline().strip().split()):
            and_result &= num
            xor_result ^= num
            if and_result & (and_result ^ xor_result):
                count += 1
        print(count % (10**9 + 7))

solve()
