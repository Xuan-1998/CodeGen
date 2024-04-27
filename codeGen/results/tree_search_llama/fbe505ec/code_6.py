def create_abbreviations(words):
    abbreviations = {}
    for word in words:
        if len(word) > 10:
            first_letter = word[0]
            last_letter = word[-1]
            length_diff = len(word) - 2
            abbreviation = f"{first_letter}{last_letter}{length_diff}"
            abbreviations[word] = abbreviation
    return abbreviations

def replace_long_words(input_list, abbreviations):
    output_list = []
    for word in input_list:
        if len(word) > 10 and word in abbreviations:
            output_list.append(abbreviations[word])
        else:
            output_list.append(word)
    return output_list

n = int(input())
words = [input() for _ in range(n)]
abbreviations = create_abbreviations(words)
output = replace_long_words(words, abbreviations)

for result in output:
    print(result)
