def check_string():
    s = input().strip()
    
    state_machine = {'A': 0, 'B': 0}
    found_ab = False
    
    for i in range(len(s)):
        if s[i] == 'A' and i + 1 < len(s) and s[i+1] == 'B':
            state_machine['B'] += 1
            found_ab = True
        elif s[i] == 'B' and i + 1 < len(s) and s[i+1] == 'A':
            state_machine['A'] += 1
            found_ab = True
        
        if not found_ab:
            continue
        
        if (state_machine['A'] > 0 and state_machine['B'] > 0) or (state_machine['A'] < 0 and state_machine['B'] < 0):
            return "NO"
        
        if s[i+1:] == 'BA' or s[i+1:] == 'AB':
            print("YES")
            return
        
    print("NO")

check_string()
