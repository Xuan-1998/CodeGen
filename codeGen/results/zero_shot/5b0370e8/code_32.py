def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 2**k - 1
        xor_result = 0
        count = 0
        for _ in range(n):
            x = int(input())
            and_result &= x
            xor_result ^= x
        if and_result >= xor_result:
            count = (count + 1) % (10**9+7)
        print(count)

if __name__ == "__main__":
    solve()
