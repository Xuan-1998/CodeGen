Let's break down the problem into smaller sub-problems:

1. Check if all elements in the permutation p are distinct (i.e., no repeated elements).
2. If the permutation contains only one type of element, return "YES" because we can create two arrays a and b with no common elements.
3. Otherwise, sort the permutation p in ascending order.
4. Initialize an empty array b with length n.
5. Initialize an index i to 0.
6. Loop through the sorted permutation p:
   - If the current element is greater than the last element of b (if b is not empty), add it to the end of b and increment i.
   - Otherwise, if the current element is equal to the last element of b, return "NO" because we cannot merge two arrays with common elements.
7. Initialize an empty array a with length n.
8. Loop through the remaining elements in p:
   - Add them to the end of a and increment i.
9. Return "YES" if all elements in p are merged successfully.

Here is the Python code for the above steps:

