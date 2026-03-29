def STF(i):
    if i < 0:
        return (False, False)
    if i in memo:
        return memo[i]

    num_and = 0
    can_increase_bitwise_and = True

    for v in range(2**k):  # Try all possible values of the ith element
        bitwise_xor_result = v
        bitwise_and_result = v & (1 << k - 1)

        for j in range(i):
            bitwise_xor_result ^= arr[j]
            bitwise_and_result &= arr[j]

        if bitwise_and_result < bitwise_xor_result:
            num_and += STF(i - 1)[0] + STF(i - 1)[1]
            can_increase_bitwise_and = False
        else:
            num_and += STF(i - 1)[0]

    memo[i] = (num_and, can_increase_bitwise_and)
    return memo[i]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = STF(n - 1)[0]
    print(ans % (10**9 + 7))
