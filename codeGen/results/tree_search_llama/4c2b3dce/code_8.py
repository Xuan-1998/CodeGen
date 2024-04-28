def find_substrings(s):
    found_ab = False
    found_ba = False

    for i in range(len(s) - 1):
        substring = s[i:i+2]

        if substring == 'AB':
            found_ab = True
        elif substring == 'BA':
            found_ba = True

    if found_ab and found_ba:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    s = input()
    find_substrings(s)
