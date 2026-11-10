
# Experiment 5: Sum of Subsets

## Problem Statement
To find all subsets of a given set of positive
integers whose sum is equal to a specified target
value using the Backtracking technique.

## Objective
- Understand the Sum of Subsets problem.
- Apply recursive backtracking.
- Generate possible subsets.
- Find subsets satisfying the target sum.
- Understand inclusion and exclusion of elements.

## Algorithm / Approach
1. Accept a set of positive integers.
2. Specify the target sum.
3. Sort the elements.
4. Start with an empty subset and sum zero.
5. Include the current element and recursively
   explore the remaining elements.
6. Backtrack by removing the included element.
7. Explore the path that excludes the element.
8. If the current sum equals the target, store
   the subset.
9. Display all valid subsets.

## Pseudocode
START
Read set and target.
Sort the set.

Subset(index, current_sum):
    IF current_sum == target:
        Print current subset
        RETURN

    IF index == size:
        RETURN

    Include current element.
    Subset(index + 1, current_sum + element)

    Remove current element.

    Exclude current element.
    Subset(index + 1, current_sum)

Call Subset(0, 0).
STOP

## Time Complexity
O(2^N), because each element has two choices:
include or exclude.

## Space Complexity
O(N) auxiliary recursion space, excluding
the storage required for the resulting subsets.

## Result
The Sum of Subsets problem was successfully
implemented using the Backtracking technique.
