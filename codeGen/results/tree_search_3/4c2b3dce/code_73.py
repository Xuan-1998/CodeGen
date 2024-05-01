from sys import stdin

def check_substrings(s):
    n = len(s)
    
    for i in range(n-1):
        if s[i:i+2] == 'AB' and s[n-i-3:n-i-1] == 'BA':
            return "YES"
            
    return "NO"

if __name__ == "__main__":
    s = stdin.readline().strip()
    print(check_substrings(s))
