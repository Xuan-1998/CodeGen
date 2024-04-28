s = input()
if 'AB' in s and 'BA' not in s[:s.index('AB')+2] or 'BA' in s and 'AB' not in s[:s.index('BA')+2]:
    print("YES")
else:
    print("NO")
