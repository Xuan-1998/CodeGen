def solve():
    n, k = map(int, input().split())
    s = input()
    
    # Base case: If k is greater than or equal to n, we simply repeat the string
    if k >= n:
        return s * (k // n) + s[:k % n]
    
    # If k is less than n, we consider two options: 
    # 1. Deleting the last character of the string
    # 2. Duplicating the string
    
    # Option 1: Deleting the last character of the string
    if k < len(s):
        return s[:-1] * (k // (n - 1)) + s[:k % (n - 1) + 1]
    
    # Option 2: Duplicating the string
    return s * (k // n) + s[k % n:]

if __name__ == "__main__":
    print(solve())
