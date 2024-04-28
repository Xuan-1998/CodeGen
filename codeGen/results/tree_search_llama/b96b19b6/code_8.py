def remove_duplicates(input_string):
    char_frequency = {}

    for char in input_string:
        if char not in char_frequency:
            char_frequency[char] = 0

    result_string = ""

    for char in input_string:
        if char_frequency[char] == 0:
            result_string += char
            char_frequency[char] = 1

    return result_string

# Example usage
input_string = input()
print(remove_duplicates(input_string))
