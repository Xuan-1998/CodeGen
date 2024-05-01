from functools import lru_cache

@lru_cache(None)
def dfs(i, target):
    if i == len(nums) or target < 0:
        return [target] if target == 0 else []
    include = dfs(i + 1, target - nums[i])
    exclude = dfs(i + 1, target)
    return list(set([*include, *exclude]))

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    result = set()
    for i in range(2 ** n):
        subset_sum = sum([nums[j] for j in range(n) if (i & (1 << j))])
        result.add(subset_sum)
    print(' '.join(map(str, sorted(result))))

if __name__ == "__main__":
    solve()
