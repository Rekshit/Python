process = ["P1", "P2", "P3", "P4"]
at = [0, 1, 2, 4]
bt = [5, 4, 2, 1]
tq = 12

n = len(process)

rt = bt.copy()          # Remaining Time
ct = [0] * n
wt = [0] * n
tat = [0] * n
response = [-1] * n

time = 0
completed = 0
queue = []
gantt = []

# Start from earliest arrival
time = min(at)

while completed < n:
    # Add arrived processes to queue
    for i in range(n):
        if at[i] <= time and rt[i] > 0 and i not in queue:
            queue.append(i)

    if not queue:
        time += 1
        continue

    idx = queue.pop(0)

    if response[idx] == -1:
        response[idx] = time - at[idx]

    gantt.append([process[idx], time])

    exec_time = min(tq, rt[idx])
    rt[idx] -= exec_time
    time += exec_time

    # Add newly arrived processes
    for i in range(n):
        if at[i] <= time and rt[i] > 0 and i not in queue and i != idx:
            queue.append(i)

    if rt[idx] > 0:
        queue.append(idx)
    else:
        ct[idx] = time
        completed += 1

# Calculate WT & TAT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Output Table
print("Process AT BT CT TAT WT RT")
for i in range(n):
    print(f"{process[i]:<7} {at[i]:<2} {bt[i]:<2} {ct[i]:<2} {tat[i]:<3} {wt[i]:<2} {response[i]}")

print("\nTotal Waiting Time =", sum(wt))
print("Average Waiting Time =", sum(wt) / n)
print("Total Turnaround Time =", sum(tat))
print("Average Turnaround Time =", sum(tat) / n)

# Gantt Chart
print("\nGantt Chart:")
for g in gantt:
    print(f"| {g[0]} ", end="")
print("|")

for g in gantt:
    print(f"{g[1]:<5}", end="")
print(time)
