def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 2**k - 1
        xor_result = 0
        count = 0
        for _ in range(n):
            num = int(input())
            if num >= and_result:
                count += 1
            and_result &= num
            xor_result ^= num
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
