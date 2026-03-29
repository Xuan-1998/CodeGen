# Step 1: Read the input array
input_array = list(map(int, input().split()))

# Step 2: Initialize a list to store the lengths of longest increasing subsequences ending at each position
lis = [1] * len(input_array)

# Step 3: Iterate through the input array and update the lis list accordingly
for i in range(1, len(input_array)):
    for j in range(i):
        if input_array[i] > input_array[j]:
            lis[i] = max(lis[i], lis[j] + 1)

# Step 4: Return the maximum value in the lis list
print(max(lis))
