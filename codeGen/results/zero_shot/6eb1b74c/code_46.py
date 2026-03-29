import sys

def find_minimum_steps(text, strings):
    m = 0
    used = []
    
    for i in range(len(text)):
        found = False
        for j, s in enumerate(strings):
            if text[i:i+len(s)].lower() == s.lower():
                used.append((j+1, i+1))
                m += 1
                found = True
                break
        
        if not found:
            return -1
    
    print(m)
    
    for pair in used:
        print(*pair)

text = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]

find_minimum_steps(text, strings)
