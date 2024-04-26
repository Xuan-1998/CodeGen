def can_flip_to_palindrome():
    N = int(input())  # Read the length of the binary string
    S = input()  # Read the binary string

    flips = 0  # Initialize the count of flips needed
    left = 0  # Left pointer for the palindrome substring
    right = N - 1  # Right pointer for the palindrome substring

    while left < right:
        if S[left] == S[right]:  # If characters at both ends match
            left += 1  # Move the left pointer forward
            right -= 1  # Move the right pointer backward
        else:  # If characters don't match, flip the left character
            flips += 1
            left += 1

    if left == right:  # Check if the palindrome is complete (left == right)
        print("YES" if flips % 2 == 0 else "NO")  # Print the result
    else:
        print("NO")

can_flip_to_palindrome()
