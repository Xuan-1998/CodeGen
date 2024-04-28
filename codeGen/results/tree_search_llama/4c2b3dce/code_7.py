def has_substrings(s):
    n = len(s)
    ab, ba = s.find('AB'), s.find('BA')
    
    if ab != -1 and (ba == -1 or ba > ab + 2) and (n - 2 <= ba or ba < ab - 2):
        return "YES"
    elif ba != -1 and (ab == -1 or ab > ba + 2) and (n - 2 <= ab or ab < ba - 2):
        return "YES"
    
    return "NO"

# Read input from standard input
s = input()

print(has_substrings(s))
