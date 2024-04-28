import sys

def solve():
    s = input().strip()
    
    ab_count = 0
    ba_count = 0
    
    for i in range(len(s)):
        if s[i] == 'A':
            ab_count += 1
        elif s[i] == 'B':
            ba_count += 1
        
        if ab_count > 0 and ba_count > 0:
            if s[i:i+2] == "AB" or s[i:i+2] == "BA":
                print("YES")
                sys.exit(0)
    
    if ab_count > ba_count:
        for i in range(len(s) - 1):
            if s[i:i+2] == "BA":
                print("YES")
                sys.exit(0)
    elif ba_count > ab_count:
        for i in range(len(s) - 1):
            if s[i:i+2] == "AB":
                print("YES")
                sys.exit(0)
    
    print("NO")

if __name__ == "__main__":
    solve()
