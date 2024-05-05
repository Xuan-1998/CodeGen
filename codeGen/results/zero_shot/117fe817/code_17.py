python
# Step 1: Understand the problem
# Given an integer n, count the total number of digit 1 appearing 
# in all non-negative integers less than or equal to n. 

# Step 2: Generate all non-negative integers less than or equal to n
for i in range(n+1):
    # Convert each integer to a string and iterate over its digits
    for digit in str(i).zfill(10): 
        if digit == '1':
            # Increment the count of digit 1's seen so far
            total_count += 1

# Step 3: Print the total count as the output
print(total_count)
