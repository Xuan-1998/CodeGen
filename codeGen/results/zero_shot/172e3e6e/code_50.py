# We can start by defining the function that will calculate the number of good subsequences
def good_subsequences(n, a):
    # Initialize the count variable to store the result
    count = 0
    
    # Iterate over all possible lengths of subsequences from 1 to n
    for k in range(1, n+1):
        # For each length k, calculate the number of good subsequences of that length
        good_k = 1
        
        # Initialize a variable to store the current multiple of i
        mult_i = 0
        
        # Iterate over all possible elements in the subsequence of length k
        for _ in range(k):
            # If the current element is not divisible by its position, break the loop
            if a[mult_i] % (_+1) != 0:
                break
            
            # Update the multiple of i and increment the count
            mult_i = (mult_i + 1) % a[mult_i]
            good_k = (good_k * a[mult_i]) % (10**9 + 7)
        
        # Add the number of good subsequences of length k to the total count
        count = (count + good_k) % (10**9 + 7)
    
    # Return the total count modulo 10^9 + 7
    return count

# Now, we can read the input and calculate the answer
n = int(input())
a = [int(x) for x in input().split()]
print(good_subsequences(n, a))
