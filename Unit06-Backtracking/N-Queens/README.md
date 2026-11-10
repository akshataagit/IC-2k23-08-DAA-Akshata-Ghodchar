
# Experiment 2: 4-Queens Problem

## Problem Statement
To place four queens on a 4x4 chessboard so that no
two queens attack each other using Backtracking.

## Objective
- Understand the 4-Queens problem.
- Apply recursive backtracking.
- Check row, column, and diagonal constraints.
- Find a valid queen arrangement.

## Algorithm / Approach
1. Create an empty 4x4 chessboard.
2. Start placing queens from the first row.
3. Check whether a position is safe.
4. If safe, place a queen.
5. Move to the next row recursively.
6. If no valid position is found, remove the
   previously placed queen.
7. Continue until all four queens are placed.

## Pseudocode
START
Create an empty chessboard.
PlaceQueen(row):
    IF row == 4:
        RETURN TRUE
    FOR each column:
        IF position is safe:
            Place queen
            IF PlaceQueen(row + 1):
                RETURN TRUE
            Remove queen
    RETURN FALSE
Print the chessboard.
STOP

## Time Complexity
O(N!) in the standard row-by-row backtracking
approach, as each row can contain at most one queen.

## Space Complexity
O(N^2) for the chessboard.

## Result
The 4-Queens problem was successfully solved using
the Backtracking technique.


# Experiment 3: 8-Queens Problem

## Problem Statement
To place eight queens on an 8x8 chessboard such
that no two queens attack each other using
the Backtracking technique.

## Objective
- Understand the 8-Queens problem.
- Apply recursive backtracking.
- Check safe positions for queens.
- Find a valid arrangement on the chessboard.

## Algorithm / Approach
1. Initialize an empty 8x8 chessboard.
2. Start placing queens row by row.
3. Check whether the current position is safe.
4. Place the queen if the position is valid.
5. Recursively move to the next row.
6. If no valid position exists, remove the queen.
7. Continue until all eight queens are placed.

## Pseudocode
START
Create an 8x8 chessboard.
PlaceQueen(row):
    IF row == 8:
        RETURN TRUE
    FOR col = 0 TO 7:
        IF position is safe:
            Place queen
            IF PlaceQueen(row + 1):
                RETURN TRUE
            Remove queen
    RETURN FALSE
Print the solution.
STOP

## Time Complexity
O(N!) in the standard row-by-row backtracking
approach.

## Space Complexity
O(N^2) for the chessboard.

## Result
The 8-Queens problem was successfully implemented
using the Backtracking technique.



# Experiment 4: N-Queens Problem

## Problem Statement
To implement the generalized N-Queens problem
using Backtracking, where N queens are placed on
an N x N chessboard without attacking each other.

## Objective
- Understand the generalized N-Queens problem.
- Implement a dynamic chessboard.
- Apply recursive backtracking.
- Find a valid arrangement for a user-defined N.

## Algorithm / Approach
1. Accept the value of N from the user.
2. Create an N x N empty chessboard.
3. Start placing queens from row zero.
4. Check the column and both diagonals.
5. If a position is safe, place a queen.
6. Recursively process the next row.
7. If the placement fails, remove the queen.
8. Print the solution if all queens are placed.

## Pseudocode
START
Read N.
Create an N x N board.
PlaceQueen(row):
    IF row == N:
        RETURN TRUE
    FOR col = 0 TO N-1:
        IF position is safe:
            Place queen
            IF PlaceQueen(row + 1):
                RETURN TRUE
            Remove queen
    RETURN FALSE
Display solution or no solution.
STOP

## Time Complexity
O(N!) for the standard row-by-row
backtracking approach.

## Space Complexity
O(N^2) for the chessboard, with O(N)
recursive stack space.

## Result
The generalized N-Queens problem was successfully
implemented using Backtracking.
