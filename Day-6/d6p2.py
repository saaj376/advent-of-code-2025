def solve2(filename):
    with open(filename) as f:
        rows = [l.rstrip("\n") for l in f]

    R = len(rows)
    C = max(len(r) for r in rows)

    def get(r, c):
        if c < len(rows[r]):
            return rows[r][c]
        else:
            return " "

    cols = []
    for c in range(C):
        s = ""
        for r in range(R):
            s += get(r, c)
        cols.append(s)

    probs = []
    block = []
    for col in cols:
        if col.strip():
            block.append(col)
        else:
            if block:
                probs.append(block)
                block = []
    if block:
        probs.append(block)

    total = 0
    for block in probs:
        for col in block:
            if col[-1] in "+*":
                op = col[-1]
                break

        nums = []
        for col in block:
            d = col[:-1].strip()
            if d.isdigit():
                nums.append(int(d))

        if op == "+":
            s = 0
            for n in nums:
                s += n
            total += s
        else:
            p = 1
            for n in nums:
                p *= n
            total += p

    return total

print(solve2("input.txt"))
