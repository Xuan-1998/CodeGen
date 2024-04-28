def test_algorithm(input_string):
    bear_occurrences = set()
    for i in range(len(input_string) - 3):  # because 'bear' has 4 characters
        if input_string[i:i+4] == 'bear':
            bear_occurrences.add(i)
    
    count = 0
    for i in bear_occurrences:
        for j in bear_occurrences:
            if i < j:  # avoid duplicates and non-overlapping pairs
                count += 1
    
    return count

input_string = input()
print(test_algorithm(input_string))
