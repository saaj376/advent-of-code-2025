def counttotalzeroes(filename):
    start=50
    total=0
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            distance=int(line[1:])
            direction=line[0]
            
            if direction=='R':
                step=1
            else:
                step=-1

            for i in range(distance):
                start=(start+step)%100
                if start==0:
                    total+=1
    return total

filename="input.txt"
print(counttotalzeroes(filename))