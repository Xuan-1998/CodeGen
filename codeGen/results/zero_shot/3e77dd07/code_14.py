def are_scrambled(s1, s2):
    def construct_tree(s):
        if len(s) == 0:
            return None
        mid = len(s) // 2
        return {'left': construct_tree(s[:mid]), 'right': construct_tree(s[mid:])}

    def is_scramble(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1['left'] is None and t2['right'] is None and t1['right'] is None and t2['left'] is None:
            return t1['left'] == t2['right']
        if t1['left']['left'] is None and t2['right']['right'] is None and t1['left']['right'] is None and t2['right']['left'] is None:
            return t1['left']['left'] == t2['right']['right'] and t1['left']['right'] == t2['right']['left']
        if are_scramble(t1['left'], t2['right']) and are_scramble(t1['right'], t2['left']):
            return True
        return False

    t1 = construct_tree(s1)
    t2 = construct_tree(s2)

    return is_scramble(t1, t2)


# Test the function
s1 = input()
s2 = input()

print(are_scrambled(s1, s2))
