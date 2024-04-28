def find_AB_BA(s):
    n = len(s)
    
    # Initialize the dictionary to store the results for substrings
    memo = {}
    
    def check_substring(start, end):
        # Check if the substring 'AB' or 'BA' is present in the remaining part of the string
        if start + 2 <= end:
            if s[start:start+2] == 'AB' and s[end-1:end+1] == 'BA':
                return True
            elif s[start:start+2] == 'BA' and s[end-1:end+1] == 'AB':
                return True
        return False
    
    for i in range(n):
        if (i, n) not in memo:
            memo[(i, n)] = check_substring(i, n)
        
        if memo[(i, n)]:
            print("YES")
            return
        
    print("NO")

# Read the input string from standard input
s = input()

find_AB_BA(s)
