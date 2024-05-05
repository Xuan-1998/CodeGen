def find_count(n):
    dp = [0]  # Initialize the dynamic programming array with an empty list

    for i in range(1, n+1):  # Iterate over all numbers from 1 to n
        if bin(i).count('1') == 1:  # Check if the binary representation of i contains exactly one '1'
            dp.append(dp[-1] + 1)  # If it does, increment the count by 1 and append it to the dynamic programming array
        else:
            dp.append(dp[-1])  # If it doesn't, keep the previous count

    return dp[-1]  # Return the last element of the dynamic programming array, which is the final answer

n = int(input())  # Read n from standard input
print(find_count(n))  # Print the result
