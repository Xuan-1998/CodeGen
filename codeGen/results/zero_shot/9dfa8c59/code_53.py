def get_permutations(n):
    str_n = str(n)
    if len(str_n) == 1:
        return [str_n]
    
    perms = []
    for i in range(len(str_n)):
        remaining_digits = str_n[:i] + str_n[i+1:]
        for p in get_permutations(int(remaining_digits)):
            perms.append(str_n[i] + p)
    
    return perms
