def generate_collections(current_collection, index):
    if index == len(arr):  # base case: we've reached the end of the array
        return {tuple(current_collection)}  # return the current collection as a tuple

    ways = set()  # initialize the set to store all possible collections
    for i in range(index, n):
        new_collection = current_collection + [arr[i]]  # add the current element to the collection
        ways.update(generate_collections(new_collection, i+1))  # recursively generate collections

    return ways

def count_ways():
    total_ways = set()  # initialize the set to store all possible collections
    for i in range(n):
        ways = generate_collections([], i)  # generate all possible collections starting from element i
        total_ways.update(ways)  # update the total set of ways

    return len(total_ways) % (10**9 + 7)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_ways())

if __name__ == "__main__":
    main()
