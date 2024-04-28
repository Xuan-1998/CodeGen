def check_string(s):
    A_count = 0
    B_count = 0

    for char in s:
        if char == 'A':
            A_count += 1
        elif char == 'B':
            B_count += 1

    if A_count - B_count == 1:  # If 'A's appear more frequently
        return "YES" if B_count >= 1 else "NO"
    elif B_count - A_count == 1:  # If 'B's appear more frequently
        return "YES" if A_count >= 1 else "NO"

    return "YES" if A_count >= 1 and B_count >= 1 else "NO"


