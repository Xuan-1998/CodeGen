import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    max_val = 0
    
    # Generate all possible substrings and calculate their bitwise OR
    for i in range(n):
        for j in range(i+1, n+1):
            sub1 = int(s[i:j], 2)
            for k in range(j, n+1):
                sub2 = int(s[j:k], 2)
                max_val = max(max_val, sub1 | sub2)
    
    # Print the maximum possible value
    print(bin(max_val)[2:])

if __name__ == "__main__":
    solve()
