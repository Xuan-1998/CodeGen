def solve(n, k, a):
    and_result = ((1 << k) - 1)
    xor_result = (1 << k) - 1
    count = 0
    for i in range(1 << k):
        bits = bin(i)[2:].zfill(k)
        if all((i & j) == 0 for j in a) and ((i ^ and_result) & (xor_result ^ and_result)) == 0:
            count += 1
    return count % (10**9 + 7)

count_satisfying_arrays()
