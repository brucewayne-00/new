

process=[(1,2,3),(2,0,4),(3,5,7)] #id, arrival time, burst time

process.sort(key=lambda x:(x[0],x[1]))
time=0
for p in process:
    start=max(time, p[1])
    time=start+p[2] 
    print(f"process {p[0]} started at {start} and finished at {time}")

