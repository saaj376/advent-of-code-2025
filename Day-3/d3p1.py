def totaljoltage(filename):
    total=0
    with open(filename,'r') as f:
        for i in f:
            line=i.strip()
            if not line:
                continue
            digits=[]
            for char in line:
                digit=int(char)
                digits.append(digit)
            n=len(digits)
            max=0
            for j in range(n):
                for k in range(j+1,n):
                    joltage=10*digits[j]+digits[k]
                    if joltage>max:
                        max=joltage
            total+=max
    return total
print(totaljoltage("input.txt"))