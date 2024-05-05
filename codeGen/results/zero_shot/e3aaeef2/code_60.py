# Step 1: Understand the problem
def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Step 2: Apply operations to the number
        for _ in range(m):
            n = str(n)
            n = ''.join(str(int(digit) + 1) if digit != '9' else '0' for digit in n)
            n = int(n)
        
        # Step 3: Calculate the length of the resulting number modulo 10^9+7
        print((len(str(n)) % (10**9 + 7)))
