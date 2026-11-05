
def job_sequencing(jobs):

    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create empty time slots
    slots = [None] * max_deadline

    total_profit = 0
    count = 0

    for job_id, deadline, profit in jobs:

        # Find the latest available slot
        for j in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[j] is None:

                slots[j] = job_id
                total_profit += profit
                count += 1

                break

    print("\nSelected Jobs:")

    for job in slots:
        if job is not None:
            print(job, end=" ")

    print("\nNumber of Jobs:", count)
    print("Maximum Profit:", total_profit)


# Main program
n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):

    job_id, deadline, profit = input(
        "Enter job ID, deadline and profit: "
    ).split()

    jobs.append((job_id, int(deadline), int(profit)))

job_sequencing(jobs)
