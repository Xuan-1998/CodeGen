def max_common_substrings():
    str1 = input().strip()
    str2 = input().strip()

    result = set()
    for i in range(len(str1)):
        for j in range(i+1, len(str2)+1):
            if str1[i:j] in recursive_max_common_substrings(i, j, {}):
                result.add(str1[i:j])
    
    print(len(result))

if __name__ == "__main__":
    max_common_substrings()
