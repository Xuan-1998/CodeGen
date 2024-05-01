def check_string():
    s = input().strip()
    
    for i in range(len(s)-2):  # We need at least three characters to form 'AB' or 'BA'
        if s[i:i+2] == "AB" and s[i+2:] == "BA":
            print("YES")
            return
        elif s[i:i+2] == "BA" and s[i+2:] == "AB":
            print("YES")
            return
    
    print("NO")

check_string()
