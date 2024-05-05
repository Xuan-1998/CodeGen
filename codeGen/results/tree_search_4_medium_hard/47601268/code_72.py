def count_binary_without_consecutive_ones(n):
    memo = {0: 1}
    for i in range(1, n+1):
        if i % 2 == 0:
            memo[i] = memo[i//2] + memo.get(i-1, 0)
        else:
            memo[i] = memo[(i-1)//2] + (memo.get((i-1)//2, 0) if i>1 else 1)
    return memo[n]

n = int(input())
print(count_binary_without_consecutive_ones(n))
