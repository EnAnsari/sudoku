**Method 2:** ***Backtracking***

**Complexity Analysis**

-   **Time complexity:**  O(9^(n\*n)).<br>
    For every unassigned index, there are 9 possible options so the time complexity is O(9^(n\*n)). The time complexity remains the same but there will be some early         pruning so the time taken will be much less than the naive algorithm but the upper bound time complexity remains the same.
-   **Space Complexity:**  O(n\*n).<br>
    To store the output array a matrix is needed.

**Approach**

Like all other Backtracking problems, Sudoku can be solved by one by one assigning numbers to empty cells. Before assigning a number, check whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.

**Algorithm** 

1. Create a function that checks after assigning the current index the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true; hashMap can be avoided by using loops.
2. Create a recursive function that takes a grid.
3. Check for any unassigned location. If present then assign a number from 1 to 9, check if assigning the number to current index makes the grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9. if any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.
4. If there is no unassigned location then return true.
