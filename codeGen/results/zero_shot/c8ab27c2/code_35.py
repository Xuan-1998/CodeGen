s = input()
t = input()
seen = set(t)
ans = float('inf')
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if "".join(s[i:j]) not in seen:
            ans = min(ans, j-i)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
