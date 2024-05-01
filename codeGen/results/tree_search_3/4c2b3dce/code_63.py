from collections import Counter

def solve():
    s = input().strip()
    count = Counter(s)
    
    if count['A'] >= 1 and count['B'] >= 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
