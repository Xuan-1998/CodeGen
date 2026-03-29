def bitwise_and_xor(arr):
    and_result = arr[0]
    xor_result = arr[0]
    for num in arr[1:]:
        and_result &= num
        xor_result ^= num
    return and_result, xor_result

def count_arrays(n, k):
    max_and = (1 << k) - 1
    max_xor = max_and ^ ((1 << k) - 1)
    if max_and >= max_xor:
        return pow(2, n, 10**9 + 7) % (10**9 + 7)
    else:
        return 0

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_arrays(n, k))
