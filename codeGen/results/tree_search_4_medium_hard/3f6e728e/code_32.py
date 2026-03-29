def find_upper_hemisphere(r):
    count = 0
    for u in U:
        if u <= r:
            count += 1
    return count
