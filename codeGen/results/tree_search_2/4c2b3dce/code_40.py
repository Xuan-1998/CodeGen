import sys

def checkAB(s):
    dp = {'A': 0, 'B': 0}
    for c in s:
        if c == 'A':
            dp['A'] += 1
        elif c == 'B':
            dp['B'] += 1
    
    return (dp['A'] > 0 and dp['B'] > 0) or (s.count('AB') + s.count('BA')) >= 2

input_str = sys.stdin.readline().strip()
print("YES" if checkAB(input_str) else "NO")
