def cafeteria(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    rangeends = lines.index("")
    remaining = lines[:rangeends]
    firstset = lines[rangeends+1:]

    ranges = []
    for r in remaining:
        parts = r.split("-")
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))

    ingredients = []
    for i in firstset:
        ingredients.append(int(i))

    count = 0
    for i in ingredients:
        isfresh = False
        for (a, b) in ranges:
            if a <= i <= b:
                isfresh = True
                break
        if isfresh:
            count += 1

    return count


print(cafeteria("input.txt"))
