import sys

def solve():
    s = input().strip()
    ab_found = False
    ba_found = False
    
    for i in range(len(s)):
        if (i + 1 >= len(s) or s[i:i+2] != "AB") and (i + 2 >= len(s) or s[i+1:i+3] != "BA"):
            continue
        
        if s[i:i+2] == "AB":
            ab_found = True
        else:
            ba_found = True

    if ab_found and ba_found:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
