process = ["P1", "P2", "P3", "P4"]
at = [0, 1, 2, 4]
bt = [5, 3, 4, 1]

n = len(process)

rt = bt.copy()             # Remaining Time
ct = [0] * n
wt = [0] * n
tat = [0] * n
response = [-1] * n        # Response Time

time = 0
completed = 0
gantt = []

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

    if response[idx] == -1:
        response[idx] = time - at[idx]

    if not gantt or gantt[-1][0] != process[idx]:
        gantt.append([process[idx], time])

    rt[idx] -= 1
    time += 1

    if rt[idx] == 0:
        ct[idx] = time
        completed += 1

# Calculate TAT & WT
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
