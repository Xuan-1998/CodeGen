if __name__ == "__main__":
    n = int(input())
    tree = [int(x) for x in input().split()]
    result = max_sum_path(tree)
    print(result)
