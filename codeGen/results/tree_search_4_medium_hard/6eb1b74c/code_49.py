import sys

def solve(text, string_set):
    # Preprocessing: Parse the input text into a suffix tree or an automaton
    # For simplicity, let's use a naive approach and store all occurrences of each string in the set
    occurrences = {}
    for s in string_set:
        occurrs = [(i, i + len(s) - 1) for i in range(len(text)) if text[i:i+len(s)] == s]
        occurrences[s] = occurrs

    # String selection: Identify the strings that can be used to cover the most uncovered characters
    selected_strings = []
    uncovered_chars = set(range(len(text)))
    while uncovered_chars:
        best_string = None
        max_covered = 0
        for s in string_set:
            if not occurrences[s]:
                continue
            covered = len(uncovered_chars & set(occurrs) for occurrs in occurrences[s])
            if covered > max_covered:
                best_string, max_covered = s, covered
        selected_strings.append(best_string)
        uncovered_chars -= set(occurrs) for occurrs in occurrences[best_string]

    # Step counting: Count the number of steps required to color all letters of the text in red
    steps = len(selected_strings)
    print(steps)

    # Output the pairs of indices: w_j and p_j (1 <= j <= m), which denote that the string with index w_j was used as a substring to cover the occurrences starting in the text t from position p_j
    for i, s in enumerate(selected_strings):
        for start, end in occurrences[s]:
            print(f"{i+1} {start}")
