def find_smallest_string():
    n, k = map(int, input().split())
    s = input()
    
    if k >= n:
        # Duplicate the string until its length is k
        duplicated_s = s * (k // n)
        
        # Add the remaining characters from the original string (if any)
        duplicated_s += s[:k % n]
        
        # Compare with deleting the last character
        delete_last_char = s[:-1] + s[-1] * ((k - 1) // n)
        delete_last_char += s[:(k-1)%n + 1]
        
        if duplicated_s < delete_last_char:
            return duplicated_s
        else:
            return delete_last_char
    else:
        # Delete the last character of the input string (if necessary)
        delete_last_char = s[:-1] * (k // n) + s[:k % n]
        
        # Compare with duplicating the string
        duplicated_s = s * k
        
        if delete_last_char < duplicated_s:
            return delete_last_char
        else:
            return duplicated_s

print(find_smallest_string())
