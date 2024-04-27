def solve(words):
    abbreviations = []
    for word in words:
        if len(word) > 10:
            first_letter = word[0]
            last_letter = word[-1]
            middle_length = len(word) - 2
            abbreviation = f"{first_letter}{last_letter}{middle_length}"
            abbreviations.append(abbreviation)
        else:
            abbreviations.append(word)
    return abbreviations

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

print("\n".join(solve(words)))
