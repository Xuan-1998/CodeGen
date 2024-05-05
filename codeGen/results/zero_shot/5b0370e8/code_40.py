dp = [0] * (1 << k)
for i in range(2**k):
    a = [i & ((1 << k) - 1), (i >> k) & ((1 << k) - 1)]
    if and_op(a) >= xor_op(a):
        dp[i] += 1

count = sum(dp)
print(count % (10**9 + 7))
