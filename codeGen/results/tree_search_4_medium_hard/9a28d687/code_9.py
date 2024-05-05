import sys

def min_cost_to_sort(sizes, costs):
    n = len(sizes)
    memo = {}

    def dp(i, rev):
        if (i, rev) in memo:
            return memo[(i, rev)]

        if i == n:
            return 0

        ans = float('inf')
        for j in range(i + 1, n):
            if not sizes[j].startswith(sizes[i]):
                break
        else:
            return -1

        for j in range(i + 1, n):
            if rev or not sizes[j].startswith(sizes[i]):
                break
            ans = min(ans, dp(j, True) + costs[i])

        memo[(i, rev)] = ans
        return ans

    return dp(0, False)

def main():
    n = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))
    sizes = [sys.stdin.readline().strip() for _ in range(n)]

    print(min_cost_to_sort(sizes, costs))

if __name__ == "__main__":
    main()
