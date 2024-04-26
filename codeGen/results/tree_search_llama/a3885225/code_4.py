def flip_to_palindrome():
    n = int(input())
    s = input()
    
    flips = 0
    left, right = 0, n - 1
    
    while left < right:
        if s[left] != s[right]:
            flips += 1
        left += 1
        right -= 1
    
    print("YES" if flips <= n // 2 else "NO")

if __name__ == "__main__":
    flip_to_palindrome()
