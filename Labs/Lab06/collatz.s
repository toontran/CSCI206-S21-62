.data
	MAX_ITEMS: 	.word 100
	implstr: 	.asciz " ==> "
	lf:	 	.asciz "\n"

.text
main:
	li s0, 0		# Current num
	la s1, MAX_ITEMS	# Max items const

loop_1:
	addi s0, s0, 1		# Incr current num
	mv a0, s0
	jal find_length		# Outputs length of s0 at a0
	mv t1, a0		# t1 stores the output
	
	li a7, 1		# Print current num
	mv a0, s0
	ecall
	li a7, 4		# Print string " ==> "
	la a0, implstr
	ecall
	li a7, 1		# Print length
	mv a0, t1
	ecall
	li a7, 4		# Print line feed
	la a0, lf
	ecall
	
	lw t0, 0(s1)		# Compare with MAX_ITEMS
	bne s0, t0, loop_1
	
	j done
	
	
find_length:
	addi t0, zero, 1	# Length t0
	addi sp, sp, -12 	# allocate space for ra
	sw ra, 4(sp)
	sw t0, 8(sp)
	mv t1, a0		# Collatz num t1
loop:
	lw t0, 8(sp)
	addi t1, t1, -1		# Minus 1, if t1 is 1 then t1 - 1 = 0
	beq t1, zero, done_loop
	addi t1, t1, 1		# Add back 1 
	mv a0, t1		# Call collatz
	jal collatz
	mv t1, a0
	lw t0, 8(sp)		# Load current length
	addi t0, t0, 1 		# Incr length
	sw t0, 8(sp)
	j loop
done_loop:
	lw ra, 4(sp) 		# restore ra
	addi sp,sp, 12 		# deallocate space
	mv a0, t0		# Return length
	jr ra 			# return to main

collatz:
	srli t3, a0, 1		# Divide a0 by two
	add t3, t3, t3 		# Multiply t3 by two: If t3 = a0 then a0 is even, else odd
	beq t3, a0, is_even
	mv t4, a0		# t4 = a0, a0 = a0 + a0 + t4 = 3 * a0
	add a0, a0, a0
	add a0, a0, t4
	addi a0, a0, 1
	jr ra 
is_even:
	srli a0, a0, 1		# Divide by two
	jr ra
	
done:
	li	a7, 10			# exit to OS
	ecall