import itertools

def get_subsets_and_sums(subset):
    if not subset:
        return ({set()}, {0})
    subsets = []
    sums = set()
    for element in subset:
        new_subset1 = set(subset) - {element}
        new_subset2 = set(subset)
        (new_subsets, new_sums) = get_subsets_and_sums(new_subset1)
        (new_subsets2, new_sums2) = get_subsets_and_sums(new_subset2)
        for new_subset in new_subsets:
            subsets.append(new_subset | {element})
        sums.update({sum + element for sum in new_sums} | {0})
    return (set(subsets), sums)

def main():
    N = int(input())
    numbers = set(int(input()) for _ in range(N))
    dp_state = get_subsets_and_sums(numbers)
    all_sums = set()
    for subset in dp_state[0]:
        all_sums.add(sum(subset))
    print(' '.join(map(str, sorted(all_sums))))

if __name__ == '__main__':
    main()
