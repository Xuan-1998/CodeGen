code = []
start = 0
end = 0
ab_count = [0, 0]
found = False

while end < len(s):
    if s[end] == 'A':
        ab_count[1] += 1
    else:
        ab_count[0] += 1
    if ab_count[0] > 0 and ab_count[1] > 0:
        found = True
    if found:
        code.append("YES")
        break
    end += 1

if not found:
    code.append("NO")

print("\n".join(code))
