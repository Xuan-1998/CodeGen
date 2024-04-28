n = int(input())
str1 = input()
str2 = input()

def find_max_common_substrings(str1, str2):
    max_length = 0
    substrings = set()
    
    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            substring = str1[i:j]
            if substring in str2 and len(substring) > max_length:
                max_length = len(substring)
                substrings.add(substring)
                
    return len(substrings)

print(find_max_common_substrings(str1, str2))
