# Non-Preemptive SJF with Arrival Time

n = int(input("Enter number of processes: "))

process = []
arrival = []
burst = []

for i in range(n):
    process.append(f"P{i}")
    arrival.append(int(input(f"Enter arrival time of P{i}: ")))
    burst.append(int(input(f"Enter burst time of P{i}: ")))

completed = [False] * n
waiting_time = [0] * n
turnaround_time = [0] * n

time = 0
completed_count = 0
gantt = []

while completed_count < n:
    idx = -1
    min_bt = 9999

    for i in range(n):
        if arrival[i] <= time and not completed[i]:
            if burst[i] < min_bt:
                min_bt = burst[i]
                idx = i

    if idx == -1:
        time += 1
    else:
        gantt.append(process[idx])
        waiting_time[idx] = time - arrival[idx]
        time += burst[idx]
        turnaround_time[idx] = waiting_time[idx] + burst[idx]
        completed[idx] = True
        completed_count += 1

total_wt = sum(waiting_time)
total_tat = sum(turnaround_time)

avg_wt = total_wt / n
avg_tat = total_tat / n

# Output
print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(f"{process[i]}\t{arrival[i]}\t{burst[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

print("\nTotal Waiting Time =", total_wt)
print("Average Waiting Time =", avg_wt)
print("Total Turnaround Time =", total_tat)
print("Average Turnaround Time =", avg_tat)

# Gantt Chart
print("\nGantt Chart:")
for p in gantt:
    print(f"| {p} ", end="")
print("|")
