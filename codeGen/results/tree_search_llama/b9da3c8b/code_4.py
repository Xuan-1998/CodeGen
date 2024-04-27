def count_untreated_crimes(events):
    available_officers = 0
    untreated_crimes = 0
    for event in events:
        if event == -1:  # recruitment
            available_officers += 1
        else:  # crime occurrence
            available_officers -= 1
            if available_officers < 0:
                untreated_crimes += 1
    return untreated_crimes

n = int(input())
events = list(map(int, input().split()))
print(count_untreated_crimes(events))
