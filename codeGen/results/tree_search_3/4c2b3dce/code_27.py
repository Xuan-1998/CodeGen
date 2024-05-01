===CODE BLOCK===
def find_substrings():
    s = input()
    found_ab = False
    found_ba = False

    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB' and not found_ab:
            found_ab = True
        elif s[i:i+2] == 'BA' and not found_ab:
            print('NO')
            return
        elif s[i:i+2] == 'AB' and found_ab and not found_ba:
            found_ba = True
        elif s[i:i+2] == 'BA' and found_ab and not found_ba:
            print('YES')
            return

    if not found_ab or not found_ba:
        print('NO')

if __name__ == "__main__":
    find_substrings()
