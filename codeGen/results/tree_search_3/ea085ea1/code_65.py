def max_common_substrings(str1, str2):
    # Initialize the maximum count of common substrings
    max_count = 0
    
    # Create a dictionary to store the frequency of each substring
    freq_dict = {}
    
    # Initialize the left and right pointers for both strings
    left_str1_pos, left_str2_pos = 0, 0
    
    while left_str1_pos <= len(str1) - 1 and left_str2_pos <= len(str2) - 1:
        # Extract the current substring from both strings
        substr_str1 = str1[left_str1_pos:]
        substr_str2 = str2[left_str2_pos:]
        
        # Check if the current substring is common between the two strings
        if substr_str1 == substr_str2:
            # Increment the frequency of this substring in our dictionary
            freq_dict[substr_str1] = freq_dict.get(substr_str1, 0) + 1
            
            # Update the maximum count of common substrings
            max_count = max(max_count, len(freq_dict))
        
        # Move the window one step to the right for both strings
        left_str1_pos += 1
        left_str2_pos += 1
    
    return max_count

# Example usage:
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
