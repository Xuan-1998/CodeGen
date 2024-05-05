# Step 1: Initialize variables
total_count = 0
for i in range(n+1):
    # Step 2: Convert integer i to a string to easily count digit 1s
    str_i = str(i)
    # Step 3: Count the number of times digit 1 appears in str_i
    count_i = str_i.count('1')
    # Step 4: Add count_i to total_count
    total_count += count_i

# Step 5: Print the final result
print(total_count)
