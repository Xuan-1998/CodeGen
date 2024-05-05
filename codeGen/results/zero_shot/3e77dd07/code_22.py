def are_scrambled(s1, s2):
    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)

    return is_tree_equal(t1, t2)
