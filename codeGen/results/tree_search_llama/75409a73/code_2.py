import sys

def calculate_factorial():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        print(factorial)

calculate_factorial()
