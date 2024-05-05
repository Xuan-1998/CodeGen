import sys

n = int(input())
k = int(input())
s = input()

if k <= n:
    if k < n:  # This case is not mentioned explicitly, but it is handled.
        print(s[:k])
    else:
        print(s)
else:
    if s[0] == 'z':
        new_str = ''
        for char in s:
            if ord(char) - 96 >= 1:
                new_str += chr(ord(char) - 96 + 1)
            else:
                new_str += 'a'
        while len(new_str) < k:
            new_str += 'a'
    else:
        new_str = s
        while len(new_str) < k:
            new_str += s[0]
    print(min([s[:k], new_str]))
