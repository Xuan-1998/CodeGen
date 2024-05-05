def find_max_distribution_index(n, m, p):
    max_distribution_index = 0
    for labeling in generate_labelings(n, m, p):
        distribution_index = calculate_distribution_index(labeling)
        if distribution_index > max_distribution_index:
            max_distribution_index = distribution_index
    return max_distribution_index % (10**9 + 7)
