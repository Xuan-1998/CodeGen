1. Read n from input
2. Read array of n integers from input
3. If 1 is in the array, print 0 (no operations needed) and exit
4. For each adjacent pair in the array:
   a. Calculate the GCD of the pair
   b. If GCD is 1, we can make all elements 1
5. If a pair with GCD 1 is found:
   a. Calculate the minimum number of operations required
   b. Print the number of operations
6. If no such pair is found, print -1
