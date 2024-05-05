import sys

def main():
    dp = [[-1 for _ in range(n + 1)] for _ in range(len(t) + 1)]
    for i in range(1, len(t) + 1):
        dp[i][0] = i - 1
        for s_set_size in range(1, n + 1):
            s_set = set([s.strip() for s in open().readlines()[:s_set_size]])
            if all(s not in t[:i] for s in s_set):
                dp[i][s_set_size] = dp[i - 1][s_set_size]
            else:
                min_steps = i - 1
                for j, s in enumerate(s_set):
                    if s in t[:i]:
                        min_steps = min(min_steps, dp[j][s_set_size - 1] + 1)
                dp[i][s_set_size] = min_steps
    
    m = dp[-1][-1]
    if m == -1:
        print(-1)
    else:
        used_strings = []
        i = len(t) - 1
        s_set_size = n
        while m > 0:
            for j, s in enumerate(s_set):
                if s in t[i:i + len(s)] and dp[i][s_set_size] == dp[i - len(s)][s_set_size - 1] + 1:
                    used_strings.append((j + 1, i - len(s) + 1))
                    i -= len(s)
                    m -= 1
                    s_set_size -= 1
        for w, p in sorted(used_strings):
            print(f"{w} {p}")

if __name__ == "__main__":
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    main()
