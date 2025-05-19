processes = [(1, 0, 2), (2, 1, 8), (3, 2, 1), (4, 3, 3)]
processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival then burst
completed = []
time = 0
while processes:
    available = [p for p in processes if p[1] <= time]
    if not available:
        time += 1
        continue 
    shortest = min(available, key=lambda x: x[2])
    processes.remove(shortest)
    start = time
    time += shortest[2]
    print(f"Process {shortest[0]} started at {start}, finished at {time}")
