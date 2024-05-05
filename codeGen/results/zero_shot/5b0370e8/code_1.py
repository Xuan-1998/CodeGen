def solve():
    t = int(input())  # read the number of test cases
    MOD = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())  # read the number of elements and the maximum value
        arr = list(map(int, input().split()))  # read the array

        ans = 0
        for x in sorted(arr):  # sort the array
            bits_set = 0
            for i in range(k):
                if (x >> i) & 1:
                    bits_set += sum((y >> i) & 1 for y in arr[:arr.index(x)])
            ans += bits_set // 2 + 1

        print(ans % MOD)

solve()
