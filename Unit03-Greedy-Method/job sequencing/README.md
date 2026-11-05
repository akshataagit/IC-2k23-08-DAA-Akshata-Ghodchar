# Experiment: Job Sequencing with Deadlines Using Greedy Algorithm

## 1. Problem Statement

Given a set of jobs, where each job has a deadline and an associated profit, schedule the jobs to maximize the total profit.

Each job takes one unit of time, and a job must be completed on or before its deadline to earn its profit. Only one job can be performed at a time.

## 2. Algorithm / Approach

The problem is solved using the Greedy approach.

1. Sort all jobs in descending order of profit.
2. Find the maximum deadline among all jobs.
3. Create an array of time slots.
4. Select jobs in decreasing order of profit.
5. For each job, find the latest available slot before its deadline.
6. If a slot is available, schedule the job and add its profit.
7. Display the selected jobs and maximum total profit.

## 3. Pseudocode

```text
JobSequencing(jobs):

    Sort jobs in descending order of profit

    Find maximum deadline

    Create empty time slots

    totalProfit = 0

    For each job:
        For j = min(deadline, maxDeadline)-1 down to 0:

            If slot[j] is empty:
                slot[j] = job
                totalProfit += job.profit
                Break

    Display scheduled jobs
    Display totalProfit
```

## 4. Sample Input

```text
Enter number of jobs: 5

J1 2 100
J2 1 19
J3 2 27
J4 1 25
J5 3 15
```

## 5. Sample Output

```text
Selected Jobs:
J3 J1 J5

Number of Jobs: 3
Maximum Profit: 142
```

## 6. Time and Space Complexity

- Time Complexity: O(n log n + n × d), where n is the number of jobs and d is the maximum deadline.
- Space Complexity: O(d), for storing the time slots.

## 7. Conclusion

Job Sequencing with Deadlines uses the Greedy approach to maximize profit by selecting jobs in descending order of profit and scheduling each job in the latest available slot before its deadline.