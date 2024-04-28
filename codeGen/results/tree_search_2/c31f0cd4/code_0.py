if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    
    print(find_distinct_sums(nums))
