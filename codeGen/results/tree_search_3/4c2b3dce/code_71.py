import sys
from collections import defaultdict

def solve():
    s = input().strip()
    
    dp = defaultdict(bool)
    dp["start"] = True
    
    for i in range(len(s)):
        if i % 2 == 0:
            dp["AB"] = dp.get("AB", False) or (s[i:i+2] == "AB")
        else:
            dp["BA"] = dp.get("BA", False) or (s[i:i+2] == "BA")
    
    print("YES" if dp["AB"] and dp["BA"] else "NO")

if __name__ == "__main__":
    solve()
