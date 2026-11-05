
def fractional_knapsack(items, capacity):

    # Sort items by profit/weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0

    for weight, profit in items:

        if capacity == 0:
            break

        if weight <= capacity:
            # Take the complete item
            capacity -= weight
            total_profit += profit

        else:
            # Take a fraction of the item
            total_profit += (profit / weight) * capacity
            capacity = 0

    return total_profit


# Main program
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight, profit = map(int, input(
        f"Enter weight and profit of item {i + 1}: "
    ).split())

    items.append((weight, profit))

capacity = int(input("Enter knapsack capacity: "))

result = fractional_knapsack(items, capacity)

print("Maximum Profit =", result)
