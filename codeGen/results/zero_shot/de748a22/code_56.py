def solve():
    n, q = map(int, input().split())
    signs = list(input())
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        if signs[i] == '+':
            prefix_sum[i+1] = prefix_sum[i] + 1
        else:
            prefix_sum[i+1] = prefix_sum[i] - 1

    result = []
    for _ in range(q):
        l, r = map(int, input().split())
        total_sum = prefix_sum[r+1]
        if l > 0:
            total_sum -= prefix_sum[l-1]
        min_removals = abs(total_sum)
        result.append(min_removals)

    print(*result, sep='\n')

if __name__ == '__main__':
    solve()
