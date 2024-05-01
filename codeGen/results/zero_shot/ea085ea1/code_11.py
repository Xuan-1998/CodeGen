def max_common_substrings(str1, str2):
    N = len(str1)
    max_count = 0

    for i in range(N):  # generate all possible substrings
        for j in range(i+1, N+1):
            substring = str1[i:j]
            
            if substring in str2:  # check if substring is in str2
                count = 1
                pos = str2.find(substring)  # find the position of the substring

                while True:
                    if pos == -1:
                        break
                    
                    if str1.startswith(substring, i):
                        count += 1
                        pos = str2.find(substring, pos + len(substring))
                    else:
                        break
                
                max_count = max(max_count, count)
    
    return max_count

# Example usage
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
