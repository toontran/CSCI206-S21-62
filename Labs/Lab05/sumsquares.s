.data
#A:	.word 5, 4, 3, 2, 4, 1, 0 # declare array int A[]={5,4,3,2,4,1,0};
squares:	.space 400
sum:		.space 4
i:		.space 4
preidstring:
	.asciz "squares["
postidstring:
	.asciz "]= "
newline:
	.asciz "\n"
sumofsquaresstring:
	.asciz "sum of squares from 0 to 99 = "

    .globl main
	.text	
main:				# This symbols marks the first instruction of your program
	li 	s0, 0 		# store 0 in i
	la	t1, i
	sw 	s0, 0(t1)
	li 	s1, 0 		# store 0 in sum
	la	t1, sum
	sw 	s1, 0(t1)
	la	s2, squares	# A[0]
	
	li	s5, 100		# Length of array
	jal sum_squares
	
	#addi	s0, zero, 0
	#jal while_loop2
	
	j done
	
sum_squares:
	addi 	sp, sp, -8 # allocate space
	sw	ra, 4(sp)
while_loop:
	add	a0, zero, s0	# Square the index
	jal	square
	slli	t0, s0, 2	# Address incr at index s0 (s0 * 4)
	add	t0, t0, s2
	sw	a0, 0(t0)
	addi	t5, a0, 0	# t5 = square
	addi	a0, s0, 0	# Print message
	addi	a1, t5, 0
	jal 	print_elem	
	add	s1, s1, t5	# Add square to total sum
	addi 	s5, s5, -1	# Loop condition
	addi	s0, s0, 1	# Incr index
	beq	s5, zero, done_whileloop
	j 	while_loop
done_whileloop:
	lw	ra, 4(sp)
	addi 	sp,sp, 8 # deallocate space
	jr 	ra
	
	
print_elem:
	addi	t0, a0, 0
	addi	t1, a1, 0
	la	a0, preidstring
	li	a7, 4
	ecall
	add	a0, zero, t0		# print value of index
	li	a7, 1
	ecall
	la	a0, postidstring
	li	a7, 4
	ecall
	add	a0, zero, t1		# print value at index
	li	a7, 1
	ecall
	la	a0, newline
	li	a7, 4
	ecall
	jr ra

	
square:
	addi t0, a0, -1
	addi t1, a0, 0
square_loop:
	ble t0, zero, square_doneloop
	add a0, a0, t1
	addi t0, t0, -1
	j square_loop
square_doneloop:
	jr ra
	
	
done:
	la	a0, sumofsquaresstring
	li	a7, 4
	ecall
	add	a0, zero, s1		# print value of sum
	li	a7, 1
	ecall

	li	a7, 10		# system call for exit. 

	ecall			# Exit!
	ebreak
