def checkString():
    s = input()
    
    for i in range(len(s)):
        seenA = False
        seenB = False
        
        for j in range(i, len(s)):
            if s[j] == 'A':
                seenA = True
            elif s[j] == 'B' and seenA:
                seenB = True
            
            if seenA and seenB:
                break
                
        if seenA and seenB:
            print("YES")
            return
            
    print("NO")

checkString()
