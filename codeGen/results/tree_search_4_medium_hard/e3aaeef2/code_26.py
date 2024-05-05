def solve(n, m):
    MOD = 1e9 + 7
    memo = {1: 0}
    
    for _ in range(m):
        new_memo = {}
        for l, v in memo.items():
            for d in str(v):
                new_v = int(d) + 1
                if len(str(new_v)) > l:
                    continue
                new_state = (len(str(new_v)), new_v)
                new_memo[new_state] = max(new_memo.get(new_state, 0), v)
        memo = new_memo
    
    return len(str(memo[max(memo, key=lambda x: x[1])][1])) % MOD

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
