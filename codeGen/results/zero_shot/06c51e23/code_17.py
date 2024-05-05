# Step 1: Read the input
n, t = map(int, input().split())
fraction = float(input())

# Step 2: Initialize the maximum grade and the current grade
max_grade = 0
cur_grade = 0

# Step 3: Iterate over the fraction from right to left
for i in range(n-1, -1, -1):
    # Step 4: Calculate the current decimal part
    dec_part = (fraction % 10) ** (n-i)
    
    # Step 5: Update the current grade based on the rounding rules
    if dec_part >= 5:
        cur_grade += 1
    else:
        max_grade = max(max_grade, cur_grade + 1)
        cur_grade = 0
    
    # Step 6: Update the maximum grade
    max_grade = max(max_grade, cur_grade)
    
# Step 7: Print the maximum grade
print(int(max_grade))
