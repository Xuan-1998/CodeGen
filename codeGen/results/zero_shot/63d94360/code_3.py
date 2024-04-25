MOD = 1000000007

def ways(n, k, memo):
    if (n, k) in memo:
        return memo[(n, k)]
    if n == 0:
        return 1 if k == 1 else 0
    if n == 1:
        return k - 1
    res = (ways(n - 1, k, memo) * (k - 1) + ways(n - 1, k - 1, memo) * (k - 1)) % MOD
    memo[(n, k)] = res
    return res

def solve(N, K):
    memo = {}
    return ways(N, K, memo)

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(solve(N, K))

if __name__ == "__main__":
    main()
