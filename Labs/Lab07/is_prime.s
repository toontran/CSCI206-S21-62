# RISCV assembly is_prime



.text

.globl is_prime



is_prime:
  li t0, 2  # current divisor
  beq a0, t0, return_true
loop:
  div t1, a0, t0  # a0 / t0
  mul t1, t1, t0
  beq t1, a0, return_false
  addi t0, t0, 1  # Incr current divisor
  beq t0, a0, return_true
  j loop

return_true:
  li a0, 1
  jr ra

return_false:
  li a0, 0
  jr ra

