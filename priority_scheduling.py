
process =[(1,2,5,4),(2,1,5,6),(3,5,7,5)]
process.sort(key =lambda x: (x[1],x[2]))

time=0
for p in process:
    start=max(time,p[1])  
    time=start+p[2]
    print(f" process {p[0]} started at {start} and finished at {time}")


