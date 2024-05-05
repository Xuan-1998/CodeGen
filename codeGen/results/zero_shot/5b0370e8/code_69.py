def count_good_arrays():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        result = 0
        for _ in range(n):
            a = sum(1 << i for i in range(k) if (2**i & int(input())) != 0)
            b = sum((2**i & int(input())) ^ 2**(k-1)) for i in range(k))
            result += (a >= b)
        print(result % (10**9+7))

if __name__ == "__main__":
    count_good_arrays()
