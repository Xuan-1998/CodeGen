from collections import defaultdict

def solve(t, s):
    n = len(s)
    dp = defaultdict(int)
    dp[0] = 0
    
    for i in range(1, len(t) + 1):
        new_dp = defaultdict(int)
        used = False
        
        for j in range(n):
            if t[i - len(s[j]):i].endswith(s[j]):
                if dp[j]:
                    new_dp[i] = max(new_dp[i], dp[j] + 1)
                    used = True
                else:
                    new_dp[i] = dp[j]
        
        if not used:
            new_dp[i] = -1
        
        dp = new_dp
    
    res = []
    i = len(t)
    
    while i > 0 and dp[i] != -1:
        for j in range(n):
            if t[i - len(s[j]):i].endswith(s[j]):
                res.append((j, i - len(s[j])))
                i -= len(s[j])
                break
        
    return dp[-1], res

def main():
    T = int(input())
    
    for _ in range(T):
        t = input().strip()
        n = int(input())
        
        s = [input().strip() for _ in range(n)]
        
        steps, res = solve(t, s)
        
        if steps == -1:
            print(-1)
        else:
            print(steps)
            for step in res:
                print(*step)

if __name__ == "__main__":
    main()
