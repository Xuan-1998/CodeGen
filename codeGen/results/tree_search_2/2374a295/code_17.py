def is_divisible(n, k):
    return n % k == 0

def dp(i, k):
    if i == 0:
        return 1
    else:
        memo = {}
        def dfs(j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == 0:
                result = 1 if is_divisible(i, 1) else 0
            elif j < i:
                result = 0
            else:
                result = 0
                for x in range(1, i+1):
                    if is_divisible(x, j) and dfs(j-1):
                        result += 1
            memo[(i, j)] = result
            return result
        return dfs(k)

def main():
    n, k = map(int, input().split())
    print(dp(n, k) % 10000007)

if __name__ == "__main__":
    main()
