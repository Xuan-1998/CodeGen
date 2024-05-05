===BEGIN PLAN===
Memoize recursive function calls by storing intermediate results in a dictionary.
state: int = 0
def dp(i, k):
    if i < 0:
        return [state]
    if (i, k) in memo:
        return memo[(i, k)]
    states = []
    for j in range(2**k): 
        bit_and = 0
        bit_xor = 0
        and_count = 0
        xor_count = 0
        for mask in range(1 << k):
            temp = (j & ((~mask) + 1))
            if not (temp & mask):
                continue
            bit_and |= temp & j
            bit_xor ^= temp & j
            and_count += 1
            xor_count += 1
        if bit_and >= bit_xor:
            states.append(state + and_count * (2**k - k) + xor_count)
    memo[(i, k)] = states
    return states

memo = {}
state: int = 0

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = dp(n-1, k)
    print(sum(1 for state in result if state >= bit_xor))
