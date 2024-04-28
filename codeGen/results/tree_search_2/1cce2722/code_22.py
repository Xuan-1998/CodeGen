def max_points(a):
    n = len(a)
    memo = [[-1 for _ in range(2)] for _ in range(sum(a) + 1)]
    for i in range(n):
        total = sum(a[:i+1])
        for j in range(2):
            if total % (j*2+3) == 0:
                memo[total][j] = max(memo[total][j], 1 + a[i])
            else:
                memo[total][j] = -1
    return max(max(row) for row in memo)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(a))
