def flip_to_palindrome():
    while True:
        N = int(input())
        S = input()
        
        if not S: break
        
        # Count the number of 1's and 0's in the string
        ones = [s.count('1') for s in zip(*[S[i:] for i in range(N)])]
        
        # The string is a palindrome if and only if all but at most one 
        # count of 1's in the ones list are equal.
        if len(set(ones)) <= 2:
            print("YES")
        else:
            print("NO")

flip_to_palindrome()
