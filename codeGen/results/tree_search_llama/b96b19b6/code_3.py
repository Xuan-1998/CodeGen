def remove_duplicates(input_str):
    char_set = set()
    result_str = ""
    
    for char in input_str:
        if char not in char_set:
            char_set.add(char)
            result_str += char
    
    return result_str

input_str = input()  # read the input string from stdin
print(remove_duplicates(input_str))  # print the resultant string to stdout
