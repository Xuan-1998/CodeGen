def crimes_gone_untreated(crimes_and_recruits):
    police_officers = []
    untreated_crimes = 0

    for event in crimes_and_recruits:
        if event == -1:  # Crime occurrence
            while len(police_officers) > 0 and police_officers[-1] >= len(police_officers):  # No officer available
                police_officers.pop()
            if not police_officers:  # No officers available, crime goes untreated
                untreated_crimes += 1
        else:
            police_officers.append(event)

    return untreated_crimes

# Example usage:
input_events = list(map(int, input().split()))
crimes_gone_untreated(input_events)
