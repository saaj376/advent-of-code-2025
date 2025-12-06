def solve_worksheet(filename):
    with open(filename) as f:
        rows=[l.rstrip("\n") for l in f]

    num_rows=len(rows)
    num_cols=max(len(r) for r in rows)

    def get(r,c):
        return rows[r][c] if c<len(rows[r]) else " "

    cols=["".join(get(r,c) for r in range(num_rows)) for c in range(num_cols)]

    problems=[];block=[]
    for col in cols:
        if col.strip():block.append(col)
        else:
            if block:problems.append(block);block=[]
    if block:problems.append(block)

    total=0
    for block in problems:
        op=next(col[-1] for col in block if col[-1] in "+*")
        nums=[]
        for r in range(num_rows-1):
            s="".join(col[r] for col in block).strip()
            if s.isdigit():nums.append(int(s))
        if op=="+":
            total+=sum(nums)
        else:
            p=1
            for n in nums:p*=n
            total+=p

    return total

print(solve_worksheet("input.txt"))
