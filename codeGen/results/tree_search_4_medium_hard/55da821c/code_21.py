def min_replanting(n, m):
    # Initialize the dp dictionary
    dp = {(0, i): 0 for i in range(1, m+1)}

    for _ in range(1, n+1):
        total_species_replanted = _
        for current_section in range(1, min(total_species_replanted + 1, m) + 1):
            # If we've already replanted all species, don't replant any more
            if total_species_replanted == m:
                dp[(total_species_replanted, current_section)] = 0
            else:
                # Calculate the minimum number of replanting needed for this state
                move_to_next_section = dp.get((total_species_replanted + 1, current_section), float('inf'))
                stay_in_same_section = dp.get((total_species_replanted, current_section), float('inf'))
                dp[(total_species_replanted, current_section)] = min(move_to_next_section, stay_in_same_section) + 1

    return dp.get((n, m), -1)
