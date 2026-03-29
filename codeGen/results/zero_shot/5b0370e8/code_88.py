def and_op(arr):
    result = arr[0]
    for num in arr[1:]:
        result &= num
    return result

def xor_op(arr):
    result = arr[0]
    for num in arr[1:]:
        result ^= num
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    counts = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        and_result = and_op(arr)
        xor_result = xor_op(arr)
        if and_result >= xor_result:
            counts += 1
    print(counts % (10**9 + 7))
