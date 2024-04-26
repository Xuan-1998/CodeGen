import random

def generate_sortable_permutation(n):
    permutation = list(range(1, n+1))
    random.shuffle(permutation)
    x = 1
    while True:
        if sort_first_x(permutation[:x]) == list(range(1, n+1)):
            return ' '.join(map(str, permutation))
        x += 1

print(generate_sortable_permutation(int(input())))
