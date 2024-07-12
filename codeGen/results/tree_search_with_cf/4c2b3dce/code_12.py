def check_subsequences(s):
    n = len(s)
    found_AB = False
    found_BA = False

    i = 0
    while i < n - 1:
        if s[i] == 'A' and s[i+1] == 'B':
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2
        elif s[i] == 'B' and s[i+1] == 'A':
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2
        else:
            i += 1

    print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()
check_subsequences(input)

