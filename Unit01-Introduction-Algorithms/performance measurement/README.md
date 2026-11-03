Measure Execution Time for Different Input Sizes and Generate Performance Graphs

1. Problem Statement

Measure and compare the execution time of iterative and recursive Binary Search for different input sizes. Store experimental results in a CSV file and generate performance graphs to visualize the comparison.

2. Algorithm / Approach

Define different input sizes such as 100, 1000, 5000, 10000, 50000, and 100000.

Generate sorted arrays for each input size.

Select a random target element.

Measure the execution time of iterative Binary Search.

Measure the execution time of recursive Binary Search.

Repeat the measurement 30 times for each input size.

Calculate the average execution time.

Store the results in a CSV file.

Generate a line graph using Matplotlib.

Compare the performance of both algorithms.

3. Pseudocode

START

DEFINE input sizes

FOR each input size n

    CREATE sorted array

    SELECT random target

    REPEAT 30 TIMES
        MEASURE iterative Binary Search time
    END REPEAT

    CALCULATE average iterative time

    REPEAT 30 TIMES
        MEASURE recursive Binary Search time
    END REPEAT

    CALCULATE average recursive time

    STORE results

END FOR

SAVE results in CSV file

GENERATE performance graph

DISPLAY graph

STOP

4. Time & Space Complexity Analysis

Algorithm

Time Complexity

Space Complexity

Iterative Binary Search

O(log n)

O(1)

Recursive Binary Search

O(log n)

O(log n)

The measurement program performs 30 repetitions for each input size. Its measured time includes the function-call and interpreter overhead of Python.

5. Sample Input / Output

The program does not require manual input.

Sample Output Format:

Input Size: 100
Iterative Time: ... microseconds
Recursive Time: ... microseconds

Input Size: 1000
Iterative Time: ... microseconds
Recursive Time: ... microseconds

Input Size: 5000
Iterative Time: ... microseconds
Recursive Time: ... microseconds

Input Size: 10000
Iterative Time: ... microseconds
Recursive Time: ... microseconds

Results saved in performance_results.csv
Graph saved as performance_graph.png

The actual execution times depend on the computer's processor, operating system, Python version, and system load.

6. Screenshots / Graphs

The program automatically generates a performance graph named:

performance_graph.png

The graph compares:

Iterative Binary Search

Recursive Binary Search

The X-axis represents input size, while the Y-axis represents average execution time in microseconds.

The experimental results are stored in:

performance_results.csv

Attach the generated graph and terminal screenshot to the practical report.

7. Experimental Results

The execution-time analysis compares iterative and recursive Binary Search for multiple input sizes.

Both algorithms have O(log n) time complexity. Their execution times generally increase slowly as the input size increases.

The iterative implementation may perform faster because it avoids recursive function-call overhead. However, the actual results depend on the execution environment.

The CSV file stores the measured results, while the generated graph provides a visual comparison of both algorithms.

8. Learning Outcomes

Learned how to measure algorithm execution time.

Understood the relationship between input size and execution time.

Compared iterative and recursive Binary Search.

Learned how to store experimental results in CSV format.

Learned how to generate graphs using Matplotlib.

Understood the difference between theoretical and experimental performance.