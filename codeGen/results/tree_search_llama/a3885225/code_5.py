def can_make_palindrome(s):
    n = len(s)
    ones = s.count('1')
    
    # If there are more than (n+1)/2 1's, it's impossible to make a palindrome.
    if ones > (n + 1) // 2:
        return False
    
    # If there are exactly (n+1)/2 1's, you can always make a palindrome by flipping the middle character.
    if ones == (n + 1) // 2:
        return True
    
    # For all other cases, it's possible to make a palindrome as long as the number of '1's is not more than n/2.
    return True


def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Length of the binary string S
        s = input()  # Binary string S
        
        if can_make_palindrome(s):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
