def count_valid_arrays(arr):
    n = len(arr)
    k = arr[0].bit_length()
    max_and = 0
    xor_sum = 0

    for i in range(n):
        max_and &= arr[i]
        xor_sum ^= arr[i]

    valid_count = 0
    for i in range(2**k):
        and_result = max_and & i
        xor_result = xor_sum ^ i
        if and_result >= xor_result:
            valid_count += 1

    return valid_count % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_valid_arrays(arr)
    print(result)
