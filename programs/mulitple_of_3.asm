multiplicand: DATA 0
multiplier: DATA 3
iterations: DATA 10
count: DATA 0
one: DATA 1

START:
LOAD multiplicand
ADD multiplier
STORE multiplicand
LOAD count
ADD one
STORE count
COMPARE iterations
JUMP_IF_ZERO END
JUMP START

END:
HALT
