import sys

def solve():
    s = input()
    
    seen_ab = False
    seen_ba = False
    
    for i in range(len(s)):
        if (i >= 2) and (s[i-1:i+1] == "AB" or s[i-1:i+1] == "BA"):
            if s[i-1:i+1] == "AB":
                seen_ab = True
            else:
                seen_ba = True
        
        if seen_ab and seen_ba:
            break
    
    if seen_ab and seen_ba:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
