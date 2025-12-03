def totaljoltage(filename):
    total=0
    with open(filename, 'r') as f:
        for line in f:
            s=line.strip()
            if not s:
                continue
            k=12
            a=len(s)-k
            stack=[]

            for i in s:
                while stack and stack[-1]<i and a>0:
                    stack.pop()
                    a-=1
                stack.append(i)
            total+=int("".join(stack[:12]))
    return total
print(totaljoltage("input.txt"))
            
