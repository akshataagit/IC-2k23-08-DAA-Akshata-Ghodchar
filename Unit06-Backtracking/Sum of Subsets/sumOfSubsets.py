
# Sum of Subsets using Backtracking

def sum_of_subsets(numbers, target):

    numbers.sort()
    solutions = []

    def backtrack(index, current_subset, current_sum):

        # Target achieved
        if current_sum == target:
            solutions.append(current_subset.copy())
            return

        # Stop if all elements are processed
        if index == len(numbers):
            return

        # Stop if sum exceeds target
        if current_sum > target:
            return

        # Include current element
        current_subset.append(numbers[index])

        backtrack(
            index + 1,
            current_subset,
            current_sum + numbers[index]
        )

        # Backtrack: exclude current element
        current_subset.pop()

        backtrack(index + 1, current_subset, current_sum)

    backtrack(0, [], 0)

    return solutions


# Main program
numbers = [10, 7, 5, 18, 12, 20, 15]
target = 35

print("Given Set:", numbers)
print("Target Sum:", target)

result = sum_of_subsets(numbers, target)

print("\nSubsets whose sum is", target, ":")

if result:
    for subset in result:
        print(subset)
else:
    print("No subset found.")
