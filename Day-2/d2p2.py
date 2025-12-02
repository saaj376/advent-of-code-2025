def is_repeated_pattern(n: int) -> bool:
    s=str(n)
    L = len(s)
    for unit in range(1, L // 2 + 1):
        if L % unit != 0:
            continue
        reps = L // unit
        if reps < 2:
            continue
        if s == s[:unit] * reps:
            return True
    return False


def sum_invalid_part2(puzzle_input: str) -> int:
    total = 0
    segments = puzzle_input.strip().split(",")
    for seg in segments:
        a_str, b_str = seg.split("-")
        start = int(a_str); end = int(b_str)
        for x in range(start, end + 1):
            if is_repeated_pattern(x):
                total += x
    return total

example ="10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,4526-8370,3095-4389,4400617-4493438"
print(sum_invalid_part2(example)) 

