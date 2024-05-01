import sys

def check_string():
    s = input().strip()

    for i in range(len(s) - 1):
        if (s[i:i+2] == 'AB' or s[i:i+2] == 'BA') and ((i == len(s) - 2 and s[i+2:] != s[:i].replace('A', 'B').replace('B', 'A')) or (i < len(s) - 2 and s[i+3:] != s[:i+2].replace('A', 'B').replace('B', 'A'))):
            print("YES")
            sys.exit()

    print("NO")

check_string()
