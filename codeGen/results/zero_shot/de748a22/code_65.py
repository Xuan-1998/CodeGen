def process_query(signs, l, r):
    # Count positive and negative signs in the given range
    pos_count = sum(1 for i in range(l-1, r) if signs[i] == '+')
    neg_count = len(signs) - pos_count

    # Update counts based on parity
    if pos_count % 2:
        pos_count -= (pos_count + neg_count) % 2
    elif neg_count % 2:
        neg_count -= (pos_count + neg_count) % 2

    # Find minimum removal count
    return min(pos_count, neg_count)
