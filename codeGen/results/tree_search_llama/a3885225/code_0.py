def can_be_palindrome():
    n = int(input())
    s = input()
    
    zeros = 0
    ones = 0
    
    for char in s:
        if char == '0':
            zeros += 1
        else:
            ones += 1
            
    return (zeros == ones) or (zeros % 2 == 0)

while True:
    n = int(input())
    
    if n == 0:
        break
        
    print("YES" if can_be_palindrome() else "NO")
