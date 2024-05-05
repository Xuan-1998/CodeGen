def solve():
    arr = [int(x) for x in input().split()]  # read array from stdin
    max_sum = max_path_sum(arr)
    print(max_sum)  # write answer to stdout

if __name__ == "__main__":
    solve()
