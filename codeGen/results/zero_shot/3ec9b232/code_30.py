
5. Time complexity: O(n*n!) where n is the size of array M
   - This is because we generate all possible permutations of the array and check each one to see if it's valid

6. Space complexity: O(n) for storing the input array and the merged array in each permutation
   - We also store the total number of permutations and the count of valid permutations

This solution has a high time complexity due to the need to generate all possible permutations, but it should still be able to solve the problem within the given constraints.
