def cafeteria(filename):
    with open(filename,'r') as f:
        lines=[line.strip() for line in f]
    ranges=[]
    for line in lines:
        if "-" not in line:
            break  
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()
    merged=[]
    for start,end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total=0
    for start,end in merged:
        total+=end-start+1
    return total
print(cafeteria("input.txt"))

