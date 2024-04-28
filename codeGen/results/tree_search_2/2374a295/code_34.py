def is_divisible(i, j):
    return i % j == 0

memo = {}

def dp(i, k):
    if (i, k) in memo:
        return memo[(i, k)]
    
    if i > n or k == 0:
        return 1
    
    result = 0
    for j in range(2, min(i, k)+1):
        if is_divisible(i, j):
            result += dp(j-1, k-j)
    memo[(i, k)] = result % 1000000007  # modulo operation to avoid overflow
    return result

n, k = map(int, input().split())
print(dp(n, k))
