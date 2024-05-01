code = '''
n, m = map(int, input().split())
dp = [(-float('inf'), -float('inf'))] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    dp[u][0] = max(dp[u][0], dp[v][0]) if u != v else 1
    dp[u][1] = max(dp[u][1], dp[v][1])

k = int(input())
p = list(map(int, input().split()))
ans = [float('inf'), float('-inf')]
for i in range(k):
    ans[0] = min(ans[0], dp[p[i]][0])
    ans[1] = max(ans[1], dp[p[i]][1])

print(*ans)
'''

from io import StringIO
import sys

old_stdin, old_stdout = sys.stdin, sys.stdout

sys.stdin = StringIO(f"{n} {m}\n" + "\n".join(f"{u} {v}" for _ in range(m)) + f"\n{k}\n{int(' '.join(map(str, p)))}")
sys.stdout = StringIO()

code_executed = compile(code, 'code', 'exec')
exec(code_executed)

sys.stdin = old_stdin
sys.stdout = old_stdout

print(*ans)
