def solution():
    s = input()
    for i in range(len(s)):
        if s[i:i+2] == 'AB':
            j = i + 2
            while j < len(s):
                if s[j:j+2] == 'BA':
                    print('YES')
                    return
                j += 1
    print('NO')

solution()
