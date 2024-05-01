from collections import defaultdict

dp_ab = defaultdict(bool)
dp_ba = defaultdict(bool)

for i, c in enumerate(s):
    if c == 'A' and dp_ba[i-1] if i > 0 else True:
        dp_ab[i] = True
    elif c == 'B':
        dp_ab[i] = any(dp_ab[j] for j in range(i))
    if c == 'B' and dp_ab[i-1] if i > 0 else True:
        dp_ba[i] = True
    elif c == 'A':
        dp_ba[i] = any(dp_ba[j] for j in range(i))

result = all(dp_ab.values()) or all(dp_ba.values())

print("YES" if result else "NO")
