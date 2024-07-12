python
def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    n = len(s)
    found_AB = False
    found_BA = False
    
    # Track positions to ensure non-overlapping
    pos_AB = -1
    pos_BA = -1
    
    for i in range(n - 1):
        if s[i:i+2] == "AB":
            if found_BA and i > pos_BA + 1:
                print("YES")
                return
            if not found_AB:
                found_AB = True
                pos_AB = i
        if s[i:i+2] == "BA":
            if found_AB and i > pos_AB + 1:
                print("YES")
                return
            if not found_BA:
                found_BA = True
                pos_BA = i
    
    print("NO")

if __name__ == "__main__":
    main()

