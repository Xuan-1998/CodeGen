n = int(input())
s = input()
a = [int(x) for x in input().split()]

ans = 0
max_len = 0
min_substrs = float('inf')

curr_substr = ''
for char in s:
    if ord(char) <= a[ord('z') - ord(char)] and len(curr_substr) + 1 <= a[ord('z') - ord(char)]:
        curr_substr += char
    else:
        ans += 1
        max_len = max(max_len, len(curr_substr))
        min_substrs = min(min_substrs, len(curr_substr))
        curr_substr = ''

ans += (0 if curr_substr == '' else 1)
max_len = max(max_len, len(curr_substr) if curr_substr != '' else 0)
min_substrs = min(min_substrs, len(curr_substr) if curr_substr != '' else 0)

print(ans % (10**9 + 7))
print(max_len)
print(min_substrs)
