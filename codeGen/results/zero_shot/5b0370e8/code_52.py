def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 0xFFFFFFFFFFFFFFFF << (k - 1)
        xor_result = 0
        counter = 0
        for _ in range(n):
            num = int(input())
            and_result &= num
            xor_result ^= num
        if and_result >= xor_result:
            counter += 1
        print(counter % (10**9 + 7))

if __name__ == "__main__":
    solve()
