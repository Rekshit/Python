# Preemptive SJF (Shortest Remaining Time First)

process = ["P1", "P2", "P3", "P4"]
at = [0, 1, 2, 4]
bt = [5, 3, 4, 1]

n = len(process)

rt = bt.copy()   # Remaining time
ct = [0] * n
wt = [0] * n
tat = [0] * n
completed = 0
time = 0

gantt = []
prev = None

while completed < n:
    idx = -1
    min_rt = 9999

    for i in range(n):
        if at[i] <= time and rt[i] > 0:
            if rt[i] < min_rt:
                min_rt = rt[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    if prev != process[idx]:
        gantt.append((process[idx], time))
        prev = process[idx]

    rt[idx] -= 1
    time += 1

    if rt[idx] == 0:
        completed += 1
        ct[idx] = time

# Calculate WT and TAT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Output
print("Process\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    print(f"{process[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("\nTotal Waiting Time =", sum(wt))
print("Average Waiting Time =", sum(wt) / n)
print("Total Turnaround Time =", sum(tat))
print("Average Turnaround Time =", sum(tat) / n)

# Gantt Chart
print("\nGantt Chart:")
for g in gantt:
    print(f"| {g[0]} ", end="")
print("|")

print(gantt[0][1], end="")
for i in range(1, len(gantt)):
    print(f"   {gantt[i][1]}", end="")
print(f"   {time}")
