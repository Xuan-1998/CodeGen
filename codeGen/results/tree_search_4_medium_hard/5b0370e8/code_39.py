import sys

def count_satisfying_arrays():
    t = int(input())
    mod = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (1 << k)
        xor_count = [0] * (1 << k)

        for _ in range(n):
            num = int(input())
            bit = bin(num)[2:].zfill(k)
            and_count[int(bit, 2)] += 1
            xor_count[int(bit, 2)] ^= num

        total_count = 0
        and_prev = and_count[0]
        for i in range(1 << k):
            and_curr = sum(and_count[j] * (i & (1 << j)) for j in range(k))
            and_prev += and_curr
            xor_curr = int(bin(xor_count[i])[2:], 2)
            total_count += min(and_prev, 2**k - 1) * xor_curr % mod

        print(total_count % mod)

if __name__ == "__main__":
    count_satisfying_arrays()
