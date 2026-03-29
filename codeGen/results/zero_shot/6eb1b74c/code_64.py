import sys

def min_steps_to_color_text(text, strings):
    # Initialize variables
    steps = 0
    used_strings = []

    # Iterate over each string in the set
    for s in strings:
        # Check if the string appears in the text
        index = 0
        while True:
            index = text.find(s, index)
            if index == -1:
                break
            # If the string is found, increment steps and update used_strings
            steps += 1
            used_strings.append((strings.index(s) + 1, index))
            index += len(s)

    # Check if all characters in text were colored
    if sum(len(s) for s in strings) * steps != len(text):
        return -1

    return str(steps)
    print(' '.join(map(str, (w + p for w, p in used_strings))))
