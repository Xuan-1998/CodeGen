code
s = input()
prefix_len = 0
while prefix_len < min(len('AB'), len('BA')) and s[prefix_len] == 'A' and s[prefix_len] == 'B':
    prefix_len += 1

if 'AB' in s[prefix_len:] or 'BA' in s[prefix_len:]:
    print("YES")
else:
    print("NO")
