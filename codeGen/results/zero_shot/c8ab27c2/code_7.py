s = input().strip()
t = input().strip()

dp1 = [0] * (len(s) + 1)
dp2 = [0] * (len(t) + 1)

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            dp2[j] = max(dp2[j], dp1[i - 1] + 1)
        else:
            dp2[j] = max(dp2[j], dp1[i])
    dp1 = [dp2[j] for j in range(len(t))]
print(min(max(dp1) - i for i in range(len(s)) if all(s[i:] != t[:j])) or -1)
