def totalrolls(filename):
    with open(filename,'r') as f:
        matrix = [list(line.strip()) for line in f]  

    rows=len(matrix)
    columns=len(matrix[0])
    total=0

    while True:
        toremove=[]

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] != '@':
                    continue

                neighbours=0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if (i, j) == (r, c):
                            continue
                        if 0<=i<rows and 0<=j<columns and matrix[i][j]=='@':
                            neighbours += 1

                if neighbours < 4:
                    toremove.append((r, c)) 

        if not toremove:
            break

        for r, c in toremove:
            matrix[r][c] = '.' 

        total += len(toremove)

    return total

print(totalrolls("input.txt"))
