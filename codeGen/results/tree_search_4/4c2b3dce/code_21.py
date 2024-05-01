def find_AB_BA(s):
    def check_half(half):
        for i in range(len(half) - 1):
            if half[i] == 'A' and half[i + 1] == 'B':
                return True
            elif half[i] == 'B' and i > 0 and half[i - 1] == 'A':
                return True
        return False

    found = False
    mid = len(s) // 2
    left_half, right_half = s[:mid], s[mid:]
    
    if check_half(left_half) or check_half(right_half):
        found = True
    
    print("YES" if found else "NO")

# Receive input from stdin and call the function
s = input()
find_AB_BA(s)
