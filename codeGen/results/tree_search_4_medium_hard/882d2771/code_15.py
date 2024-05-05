def solve():
    t, l, r = map(int, input().split())
    memo = {1: 0}
    
    def f(n):
        if n not in memo:
            min_group_size = (n + 1) // 2
            max_group_size = n - min_group_size
            memo[n] = 1 + f(min_group_size) + f(max_group_size)
        return memo[n]
    
    result = sum(t * pow(10, i) * f(i) for i in range(l-1, r+1))
    print(result % (10**9 + 7))

solve()
