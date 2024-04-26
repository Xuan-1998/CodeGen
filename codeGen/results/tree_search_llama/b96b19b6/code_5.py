def remove_duplicates(input_string):
    seen = set()
    output_string = ""
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            output_string += char
    
    return output_string

input_str = input()
print(remove_duplicates(input_str))
