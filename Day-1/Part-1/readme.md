# Day 1 — Part 1 🎄✨🔐

> A frosty puzzle at the secret North Pole entrance — a dial, a sequence of rotations, and a disguised password.

────────────────────────────────────────────────────────────────

You arrive at the secret entrance to the North Pole base ready to start decorating. The password has been moved into a safe with a single dial (numbers 0–99) and a list of rotations. Your job is to follow the rotations and count how many times the dial ends up pointing at 0. That's the real password.

────────────────────────────────────────────────────────────────

🎯 Goal
- Start with the dial pointing at **50**.
- Apply each rotation in order (L = left / toward lower numbers, R = right / toward higher numbers).
- The dial wraps around (left from 0 → 99, right from 99 → 0).
- Count how many times the dial is exactly at **0** after a rotation — that count is the password.

────────────────────────────────────────────────────────────────

🔧 Rules (quick)
- Each rotation is one line: `L<number>` or `R<number>` (example: `R48`).
- Left decreases the pointer; right increases it.
- The dial positions are modulo 100 (0..99).
- The dial starts at 50.

────────────────────────────────────────────────────────────────

🧭 Example (given)
Input:
```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

Step-by-step (brief):
- start → 50  
- L68 → 82  
- L30 → 52  
- R48 → 0      ← counts as 1  
- L5 → 95  
- R60 → 55  
- L55 → 0      ← counts as 2  
- L1 → 99  
- L99 → 0      ← counts as 3  
- R14 → 14  
- L82 → 32

Answer for example: **3**

────────────────────────────────────────────────────────────────

💡 Hints & nice math
- Treat positions modulo 100: perform +distance for R, -distance for L, then wrap with `(pos + 100) % 100`.
- You only need to track the current position and a counter for hits at 0.
- This is O(n) time and O(1) space (n = number of rotations).

────────────────────────────────────────────────────────────────

🔎 Dial visual (mini)
This small diagram is illustrative — imagine a circular dial where numbers wrap around.

           0
         /   \
       99     1
      /         \
     98         2
      \         /
       97 ...  3
         \   /
           50

(Actual dial is 0..99 in order around the circle.)

────────────────────────────────────────────────────────────────

🧪 How to run (quick local check)
1. Save your puzzle input to a file, e.g. `input.txt`.
2. Run a small script that:
   - reads each line,
   - updates position with modulo arithmetic,
   - increments a counter whenever the result is 0,
   - prints the counter.

Example Python pseudocode:
```
pos = 50
count = 0
for line in open('input.txt'):
    dir = line[0]
    dist = int(line[1:])
    if dir == 'L':
        pos = (pos - dist) % 100
    else:
        pos = (pos + dist) % 100
    if pos == 0:
        count += 1
print(count)
```

────────────────────────────────────────────────────────────────
