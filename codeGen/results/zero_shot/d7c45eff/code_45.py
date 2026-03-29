import sys
from collections import deque

def solve():
    n, k = map(int, input().split())
    s = input()

    queue = deque([(s, len(s))])  # Initialize the BFS with the original string and its length
    
    while queue:
        curr_str, curr_len = queue.popleft()
        
        if curr_len == k:  # If we have found a string of the desired length
            print(curr_str)  # Print it as the result
            return
        
        if curr_len < k:  # If we haven't reached the desired length yet
            new_str1 = curr_str[:-1]  # Create a new string by removing the last character
            queue.append((new_str1, len(new_str1)))  # Add it to the BFS
            
            new_str2 = curr_str + curr_str[-1]  # Create a new string by duplicating the last character
            queue.append((new_str2, len(new_str2)))  # Add it to the BFS

    return  # If we have exhausted all possibilities and haven't found a result yet

if __name__ == "__main__":
    solve()
