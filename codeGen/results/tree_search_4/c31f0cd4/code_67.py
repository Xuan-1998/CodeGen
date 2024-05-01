from functools import lru_cache

def solve(input_list):
    @lru_cache(None)
    def dfs(i, s):
        if i == len(input_list):
            return [s]
        res = []
        res.extend(dfs(i+1, s))
        res.extend(dfs(i+1, s + input_list[i]))
        return res

    sums = set()
    for s in dfs(0, 0):
        sums.add(s)
    return ' '.join(map(str, sorted(list(sums))))


if __name__ == "__main__":
    N = int(input())
    input_list = list(map(int, input().split()))
    print(solve(input_list))
