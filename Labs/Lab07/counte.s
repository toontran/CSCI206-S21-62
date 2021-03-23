.text

.globl counte



counte:
	li t0, 0                # Counter
    li s0, 101              # ASCII of 'e'
loop:
	lb t1, 0(a0)			# t1 = value at addr a0
	addi a0, a0, 1          # Addr of next index
    beq t1, zero, return_null
	bne t1, s0, loop
	addi t0, t0, 1
	j loop
	
return_null:	
	mv a0, t0
	jr ra
