def subset_sum_sums(N):
    memo = [[[False for _ in range(101)] for _ in range(101)] for _ in range(N+1)]

    def dp(i, j, k):
        if i == 0 or j == 0 or k == 0:
            return False
        for ai in range(N, -1, -1):
            if ai <= k and memo[i-1][j-1][k-ai]:
                return True
        return False

    distinct_sums = set()
    for j in range(N+1):
        for k in range(N+1):
            if dp(N, j, k):
                distinct_sums.add(k)

    print(' '.join(map(str, sorted(list(distinct_sums)))))

if __name__ == '__main__':
    N = int(input())
    subset_sum_sums(N)
