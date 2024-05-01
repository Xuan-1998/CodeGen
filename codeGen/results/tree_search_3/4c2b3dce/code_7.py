import sys

def solve():
    s = input().strip()
    n = len(s)
    
    for i in range(n - 1):
        if (s[i:i+2] == 'AB' and s[n-2:n] == 'BA'):
            print("YES")
            return
        elif (s[i:i+2] == 'BA' and s[n-2:n] == 'AB'):
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    solve()
