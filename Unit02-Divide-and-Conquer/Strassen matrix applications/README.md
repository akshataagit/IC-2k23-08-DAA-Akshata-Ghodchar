Experiment 6: Strassen's Matrix Multiplication

1. Problem Statement

Implement Strassen's Matrix Multiplication algorithm to multiply two matrices efficiently using the Divide and Conquer technique.

2. Algorithm / Approach

Divide both matrices into four equal-sized submatrices.

Calculate seven intermediate matrix products instead of the eight products required by conventional recursive block multiplication.

Use matrix addition and subtraction to calculate these products.

Calculate the four result submatrices.

Combine the four submatrices to obtain the final product.

The seven intermediate products are:

M1 = (A11 + A22)(B11 + B22)

M2 = (A21 + A22)B11

M3 = A11(B12 - B22)

M4 = A22(B21 - B11)

M5 = (A11 + A12)B22

M6 = (A21 - A11)(B11 + B12)

M7 = (A12 - A22)(B21 + B22)

The result matrices are:

C11 = M1 + M4 - M5 + M7

C12 = M3 + M5

C21 = M2 + M4

C22 = M1 - M2 + M3 + M6

The implementation pads matrices with zeros to a square dimension that is a power of two, then removes the padding from the final result.

3. Pseudocode

STRASSEN(A, B)

    IF matrix size = 1
        RETURN A * B

    DIVIDE A INTO A11, A12, A21, A22

    DIVIDE B INTO B11, B12, B21, B22

    CALCULATE M1, M2, M3, M4, M5, M6, M7

    CALCULATE C11, C12, C21, C22

    COMBINE RESULT MATRICES

    RETURN C

END

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(n^2.807)

Average Case

O(n^2.807)

Worst Case

O(n^2.807)

Space Complexity: O(n²) auxiliary space for the matrix storage and recursive implementation.

The time complexity is approximately O(n^2.807), which is better asymptotically than conventional matrix multiplication O(n³).

5. Sample Input / Output

Input:

Enter rows of first matrix: 2
Enter columns of first matrix: 2
Enter rows of second matrix: 2
Enter columns of second matrix: 2

Enter first matrix elements:
1 2
3 4

Enter second matrix elements:
5 6
7 8

Output:

Resultant Matrix:

[19, 22]
[43, 50]


7. Experimental Results

The Strassen algorithm successfully multiplies two matrices using seven recursive multiplication operations. It produces the correct resultant matrix and reduces the asymptotic time complexity compared to conventional matrix multiplication.

8. Learning Outcomes

Understood Divide and Conquer in matrix multiplication.

Learned matrix partitioning.

Understood matrix addition and subtraction.

Learned Strassen's seven multiplication formulas.

Understood the improvement from O(n³) to approximately O(n^2.807).