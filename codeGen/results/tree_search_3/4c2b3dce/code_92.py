import sys

def solve():
    s = input().strip()
    
    count_A_before_B = 0
    count_B_after_A = 0
    
    for char in s:
        if char == 'A':
            count_A_before_B += 1
            count_B_after_A = 0
        elif char == 'B' and count_A_before_B >= 1:
            count_B_after_A += 1
            
        if count_A_before_B >= 1 and count_B_after_A >= 1:
            print("YES")
            sys.exit(0)
    
    print("NO")

if __name__ == "__main__":
    solve()
