def totalrolls(filename):
    with open(filename,'r') as f:
        matrix=[]
        for l in f:
            line=l.strip()
            matrix.append(line)
    valid=0
    rows=len(matrix)
    columns=len(matrix[0])
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c]!="@":
                continue
            neighbours=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i==r and j==c:
                        continue
                    if 0<=i<rows and 0<=j<columns:
                        if matrix[i][j]=="@":
                            neighbours+=1
            if neighbours<4:
                valid+=1
    return valid 
print(totalrolls("input.txt"))