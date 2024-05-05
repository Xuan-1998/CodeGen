def find_longest_increasing_subsequences():
    # Read input from stdin
    arr = list(map(int, input().split()))
    
    # Preprocess the input
    index_dict = {v: i for i, v in enumerate(arr)}
    
    # Initialize variables
    longest_length = 0
    longest_count = 0
    
    # Find the longest increasing subsequences
    for end in range(len(arr)):
        count = [0] * (len(arr) + 1)
        curr_length = 0
        
        for start in range(end, -1, -1):
            if arr[start] < arr[end]:
                curr_length += 1
            else:
                curr_length = 1
            
            count[curr_length] += 1
            longest_length = max(longest_length, curr_length)
        
        # Update the count of longest increasing subsequences
        longest_count += count[longest_length]
    
    # Print the answer to stdout
    print(longest_count)

if __name__ == "__main__":
    find_longest_increasing_subsequences()
