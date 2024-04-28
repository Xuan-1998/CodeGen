import sys
from typing import TextIO

def solution(s: str) -> None:
    stdin = sys.stdin
    stdout = sys.stdout
    
    s = s.strip()
    
    if not s or len(s) < 2:
        print("NO", file=stdout)
        return
    
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB" and s[i+2:].startswith("BA"):
            print("YES", file=stdout)
            return
    
    print("NO", file=stdout)

def main() -> None:
    input_str = stdin.readline().strip()
    solution(input_str)

if __name__ == "__main__":
    main()
