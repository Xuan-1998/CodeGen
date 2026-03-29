def max_path_sum(arr):
    def max_gain(node):
        if node < 0:  # leaf node
            return 0

        left_gain = max(0, max_gain(2*node+1))
        right_gain = max(0, max_gain(2*node+2))

        price_newpath = arr[node] + left_gain + right_gain
        price_oldpath = arr[node]

        return max(price_newpath, price_oldpath)

    return max_gain(0)  # starting from the root

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(max_path_sum(arr))
