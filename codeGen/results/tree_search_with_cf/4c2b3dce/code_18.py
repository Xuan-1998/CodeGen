def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    n = len(s)
    found_AB = False
    found_BA = False
    
    i = 0
    while i < n - 1:
        if s[i:i+2] == 'AB':
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2  # Skip the next character to avoid overlap
        elif s[i:i+2] == 'BA':
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2  # Skip the next character to avoid overlap
        else:
            i += 1
    
    # Reset and check the other way around to ensure no overlap
    found_AB = False
    found_BA = False
    
    i = 0
    while i < n - 1:
        if s[i:i+2] == 'BA':
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2  # Skip the next character to avoid overlap
        elif s[i:i+2] == 'AB':
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2  # Skip the next character to avoid overlap
        else:
            i += 1

    print("NO")

if __name__ == "__main__":
    main()

