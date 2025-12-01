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
# Day 1 — Part 2 🎄✨🔐

--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

> "Due to newer security protocols, please use password method `0x434C49434B` until further notice."

This method changes the rules: count every time the dial points at `0` caused by any click — including intermediate clicks that happen during a rotation, not just the final position after each rotation.

---

🎯 Goal
- Start with the dial pointing at **50**.
- Apply each rotation in order (L = left / toward lower numbers, R = right / toward higher numbers).
- The dial wraps around (left from 0 → 99, right from 99 → 0).
- Count how many times the dial is exactly at **0** at any click (intermediate or final). That total is the password.

---

🔧 Rules (quick)
- Each rotation is one line: `L<number>` or `R<number>` (example: `R48`).
- Left decreases the pointer; right increases it.
- The dial positions are modulo 100 (0..99).
- The dial starts at 50.
- Large distances (e.g. `R1000`) may hit `0` many times — we count each hit.

---

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

Step-by-step (brief, showing where hits occur):
- start → 50  
- L68 → 82 (during this rotation it passes 0 once)  
- L30 → 52  
- R48 → 0      ← final position counts (1)  
- L5 → 95  
- R60 → 55 (during this rotation it passes 0 once)  
- L55 → 0      ← final position counts (2)  
- L1 → 99  
- L99 → 0      ← final position counts (3)  
- R14 → 14  
- L82 → 32 (during this rotation it passes 0 once)

Total: 3 hits at rotation ends + 3 intermediate hits = **6**

---

## How to think about counting — no per-click simulation

Brute-force simulating each click works, but you can count hits per rotation in O(1) time.

Given:
- start position s (0..99),
- rotation direction D in {'L','R'},
- distance d (non-negative integer),

We want the count of k in {1..d} such that the dial after k clicks equals 0.

Positions after k clicks:
- L (left): pos_k = (s - k) mod 100
- R (right): pos_k = (s + k) mod 100

Find the first positive k0 in 1..100 when pos_k == 0:
- For L: k0 ≡ s (mod 100). Use k0 = s % 100, and if that is 0 treat k0 = 100.
- For R: k0 ≡ (100 − s) (mod 100). Use k0 = (100 - (s % 100)) % 100, and if that is 0 treat k0 = 100.

Then:
- If d < k0 → 0 hits.
- Otherwise → 1 + floor((d - k0) / 100) hits (one for the first hit, plus one for every additional full 100 clicks).

This handles huge distances like `R1000` without iterating the clicks.

---

