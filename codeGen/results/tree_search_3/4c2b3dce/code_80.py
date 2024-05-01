def find_substrings(s):
    s = s.upper()
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            if s[i+2:] and s[i+2:].startswith('BA'):
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    s = input()
    find_substrings(s)
