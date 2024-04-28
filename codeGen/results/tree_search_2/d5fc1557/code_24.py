def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    result = longest_ones(nums)
    print(result)

if __name__ == "__main__":
    main()
