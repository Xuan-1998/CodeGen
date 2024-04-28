def untreated_crimes(hiring_dates):
    # Initialize the number of available officers and the number of crimes that will go untreated
    available_officers = 0
    untreated_crimes_count = 0

    for date in hiring_dates:
        if date == -1:  # Crime has occurred
            available_officers += 1  # Increase the number of available officers
            if available_officers <= 0:  # If there are no available officers, increment the count of untreated crimes
                untreated_crimes_count += 1
        else:
            available_officers -= date  # Decrease the number of available officers by the number of officers hired

    return untreated_crimes_count


# Read input from stdin
n = int(input())
hiring_dates = list(map(int, input().split()))

print(untreated_crimes(hiring_dates))
