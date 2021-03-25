.text

.globl matrix_sum



matrix_sum:
    li t0, 2                # num rows
    li t1, 3                # num cols
    mul t2, t1, t0          # Max index
	li t0, 0                # Index
  
loop:    
	lw t1, 0(a0)			# A
    lw t3, 0(a1)            # B
    add t4, t1, t3         # C = A + B
    sw t4, 0(a2)
	addi a0, a0, 4          # Addr of next index
    addi a1, a1, 4
    addi a2, a2, 4
    addi t0, t0, 1
    bge t0, t2, break_loop
	j loop
	
break_loop:	
	jr ra
