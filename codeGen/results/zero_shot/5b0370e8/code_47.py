def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        and_result = 0xfffffffffffffffd >> (k - bit_length(arr[0]))
        xor_result = sum(1 << i & arr[i] for i in range(n))
        count = sum((and_result | i) >= xor_result for i in range(2**k))
        print(count % 10**9 + 7)
