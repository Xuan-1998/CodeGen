import sys

def find_smallest_string():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    if k <= n:
        # Check if the last character can be deleted to form a smaller string of length k
        if len(s) > k and s[k-1] < s[-1]:
            return s[:k]
        
        # If not, duplicate the string until we get a string of length k or less
        new_s = ""
        for i in range(n):
            new_s += s[i % n]
            if len(new_s) >= k:
                break
        
        # Return the lexicographically smallest string of length k
        return min([new_s[:k], new_s[1:k]])

k = int(sys.stdin.readline().strip())
print(find_smallest_string())
