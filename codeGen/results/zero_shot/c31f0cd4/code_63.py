n = int(input())
arr = list(map(int, input().split()))
dp = {}
ans = set()
def dfs(i, s):
    if i == n:
        ans.add(s)
    else:
        dfs(i + 1, s)
        dfs(i + 1, s + arr[i])
print(' '.join(map(str, sorted(ans))))
