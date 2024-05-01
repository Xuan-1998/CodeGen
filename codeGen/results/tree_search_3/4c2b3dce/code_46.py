import sys

def solve():
    s = input().strip()
    a_count, b_count = 0, 0
    
    for char in s:
        if char == 'A':
            a_count += 1
            if a_count == 1 and b_count == 1: 
                print("YES")
                return
        elif char == 'B':
            b_count += 1
            if a_count == 1 and b_count == 1:
                print("YES")
                return
        
    print("NO")

if __name__ == "__main__":
    solve()
