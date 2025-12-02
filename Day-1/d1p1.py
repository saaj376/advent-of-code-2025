def countzero(filename):
    dial=50
    count=0
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            direction=line[0]
            distance=int(line[1:])
            if direction=='R':
                dial=(dial+distance)%100
            else:
                dial=(dial-distance)%100
            if dial==0:
                count+=1

    return count

filename="part-1.txt"
print(countzero(filename))
