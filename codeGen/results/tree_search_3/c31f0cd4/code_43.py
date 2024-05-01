import sys

def gen_sums(current_sum, current_subset, max_sum):
    if current_sum >= max_sum:
        return []

    seen_sums_set = {current_sum}
    new_sums_set = set()

    for num in current_subset:
        new_current_sum = current_sum + num
        if new_current_sum > max_sum:
            continue

        new_sums_set.update(gen_sums(new_current_sum, current_subset - {num}, max_sum))
        seen_sums_set.add(new_current_sum)

    return sorted(list(seen_sums_set | new_sums_set))

def main():
    n = int(sys.stdin.readline())
    nums = set(int(x) for x in sys.stdin.readline().split())

    result_list = []

    for _ in range(n):
        current_sum = 0
        current_subset = set(nums)
        max_sum = sum(nums)

        result_list.append(gen_sums(current_sum, current_subset, max_sum))

    print(' '.join(map(str, sorted(set(sum(x) for x in result_list)))))

if __name__ == "__main__":
    main()
