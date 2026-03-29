import sys

def dp(bit, ones):
    if bit >= k:
        return 1 if all(ones[i] == 0 for i in range(n)) else 0

    res = [0] * (2 ** k)
    for i in range(2 ** k):
        temp = []
        and_bit = [(a >> bit) & 1 for a in arr]
        xor_bit = sum(xor(a, b) for a, b in zip(arr, [i << bit]))
        if all(and_bit):  # All bits are set
            for j in range(k):
                if ((i >> j) & 1):
                    temp.append(ones[j] + 1)
                else:
                    temp.append(ones[j])
        elif sum(xor_bit) == 0:  # No bits are set
            temp = [ones[i]] * k
        else:  # Exactly one bit is set
            for j in range(k):
                if ((i >> j) & 1):
                    temp.append(ones[j] + 1)
                else:
                    temp.append(ones[j])
        res[i] += dp(bit + 1, tuple(temp))

    return sum(res)

def xor(a, b):
    return a ^ b

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(dp(0, [0] * k) % (10 ** 9 + 7))
