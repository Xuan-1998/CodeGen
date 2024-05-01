code = input().strip()
ab_seen = ba_seen = False

for i in range(len(code)):
    if i + 2 <= len(code) and code[i:i+2] == 'AB':
        ab_seen = True
    elif i >= 1 and code[i-1:i+1] == 'BA':
        ba_seen = True

if (ab_seen and not ba_seen) or (ba_seen and not ab_seen):
    print("YES")
else:
    print("NO")
