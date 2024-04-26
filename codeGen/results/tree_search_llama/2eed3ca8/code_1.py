def is_circular(moves):
    n = len(moves)
    bad_char_table = [n] * 128  # ASCII characters + 1 (for non-alphabetic characters)

    for i in range(n - 1, -1, -1):
        for j in range(i):
            if moves[j] == moves[i]:
                bad_char_table[ord(moves[i]) - ord('a')] = i
                break

    rightmost_occurrence = n
    for c in moves:
        occurrence = bad_char_table[ord(c) - ord('a')]
        if occurrence < rightmost_occurrence:
            rightmost_occurrence = occurrence
        else:
            return "Circular"

    return "Not Circular"

moves = input().strip()
print(is_circular(moves))
