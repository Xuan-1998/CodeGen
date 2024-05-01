import sys

def find_substrings():
    s = input().strip()
    
    if 'AB' in s and 'BA' in s:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    find_substrings()
