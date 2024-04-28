def max_partition_size():
    t = int(input())  # Read the number of test cases

    for _ in range(t):
        n = int(input())  # Read the size of the array
        arr = list(map(int, input().split()))  # Read the array elements

        total_sum = sum(arr)  # Calculate the total sum of the array
        left_sum = 0  # Initialize the sum of elements on the left subarray
        max_partition_size = 0  # Initialize the maximum partition size

        for i in range(n):
            if left_sum == (total_sum - left_sum):  # Check if the sums are equal
                max_partition_size += 1  # If they are, increment the partition size
            left_sum += arr[i]  # Update the sum of elements on the left subarray

        print(max_partition_size)  # Print the maximum partition size


if __name__ == "__main__":
    max_partition_size()
