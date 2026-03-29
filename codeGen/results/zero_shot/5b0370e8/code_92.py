import sys

def count_and_xor(arr):
    and_val = arr[0]
    xor_val = 0
    for num in arr:
        and_val &= num
        xor_val ^= num
    return and_val >= xor_val

def generate_arrays(n, k):
    max_power_of_two = 2**k - 1
    all_bits = [int('1' * (k - i) + '0' * i, 2) for i in range(k)]
    arrays = []
    for mask in all_bits:
        array = [mask >> i & 1 for i in range(n)]
        if all(array):
            arrays.append(array)
    return arrays

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        arrays = generate_arrays(n, k)
        and_xor_count = sum(1 for arr in arrays if count_and_xor(arr))
        print((and_xor_count % (10**9 + 7)))

if __name__ == '__main__':
    solve()
