import sys

def check_string(s):
    if 'AB' in s and 'BA' not in s[:s.index('AB')]:
        return "YES"
    elif 'BA' in s and 'AB' not in s[:s.index('BA')]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    s = input()
    print(check_string(s))
