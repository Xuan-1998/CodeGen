python
def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    n = len(s)
    
    if n < 4:
        print("NO")
        return
    
    found_AB = False
    found_BA = False
    
    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2  # skip next character to ensure non-overlapping
        elif s[i:i+2] == "BA":
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2  # skip next character to ensure non-overlapping
        else:
            i += 1
    
    # If we reach here, it means we didn't find the required subsequences
    print("NO")

if __name__ == "__main__":
    main()

