# Experiment: Fractional Knapsack Using Greedy Algorithm

## 1. Problem Statement

Given a set of items, where each item has a specific weight and profit, and a knapsack with a fixed capacity, find the maximum possible profit.

In the Fractional Knapsack problem, we are allowed to take fractions of items. The objective is to maximize the total profit without exceeding the knapsack capacity.

## 2. Algorithm / Approach

The Fractional Knapsack problem is solved using the Greedy approach.

1. Calculate the profit-to-weight ratio for every item.
2. Sort all items in descending order of their profit-to-weight ratio.
3. Start selecting items from the highest ratio.
4. If the complete item fits into the knapsack, take the entire item.
5. Otherwise, take only the fraction that fits.
6. Calculate and display the total profit.

## 3. Pseudocode

```text
FractionalKnapsack(items, capacity):

    Sort items by profit/weight ratio in descending order

    totalProfit = 0

    For each item:
        If capacity == 0:
            Break

        If item.weight <= capacity:
            capacity = capacity - item.weight
            totalProfit += item.profit

        Else:
            totalProfit += (item.profit / item.weight) * capacity
            capacity = 0

    Return totalProfit
```

## 4. Sample Input

```text
Enter number of items: 3
Enter weight and profit of item 1: 10 60
Enter weight and profit of item 2: 20 100
Enter weight and profit of item 3: 30 120
Enter knapsack capacity: 50
```

## 5. Sample Output

```text
Maximum Profit = 240.0
```

## 6. Time and Space Complexity

- Time Complexity: O(n log n), due to sorting.
- Space Complexity: O(n), for storing the items.

## 7. Conclusion

The Fractional Knapsack problem is solved efficiently using the Greedy algorithm. By selecting items with the highest profit-to-weight ratio first, we obtain the maximum possible profit.