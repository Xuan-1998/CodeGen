alternating = True

for i in range(1, len(p)):
    if (p[i] - p[i-1]) * (p[i-2] - p[0]) <= 0:
        alternating = False
        break

if not alternating:
    print("NO")
else:
    print("YES")
