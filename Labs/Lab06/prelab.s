# File: prelab.s
# CSCI 206
# Lab 06
# Spring 2020
# Originally by Professor Guattery and Professor Meng in spring 2011
# Revised: Xiannong Meng
# 02/20/2016
# 2019-11-04 for RISC-V
#
# Student name: Tung Tran
#
# This simple program demonstrates writing very simple leaf procedures.
# The program computes an expression in the form of "4x - (2y + C)".
# You are to the procedure "myFunc", taking two parameters (x and y) and
# produce "4x - (2y + C)" within the procedure.
# See detailed instructions in lab handout.

	.data
# Define the constant c here
C:	.word	1

	.text
# The main() procedure calls my_func twice, storing the results into s0 and s1
main:
	# Call my_func(2, 3) storing result in s0 [s0 = 4*2 - (2*3 + 1) = 1]
	addi	a0, zero, 2		# load 2 (x) into a0
	addi	a1, zero, 3		# load 3 (y) into a1
	jal	my_func			# Value of ra is the next line
	add	s0, zero, a0		# store result in s0

	# Call my_func(5, 6) storing result in s1 [s1 = 4*5 - (2*6 + 1) = 7]
	addi	a0, zero, 5
	addi	a1, zero, 6
	jal	my_func			# Value of ra is the next line
	add	s1, zero, a0

	#
	# Add code here to print the result of my_func(2,3) + my_func(5,6)
	#
	add 	a0, s0, s1
	li	a7, 1
	ecall
	
		
	# The program is finished. Tell the "Operating System" that we wish to exit.
	# We'll learn more about this syntax later this week
	addi	a7, zero, 10		# system call for exit
	ecall

# my_func = 4x - (2y + C)
# Because this function modifies only a0, there is no need
# to create an activation frame
my_func:
	add	t0, a0, a0	# 4x
	add	t0, t0, t0
	
	add	t1, a1, a1	# 2y

	la	t2, C		# C
	lw	t2, 0(t2)
	
	add 	t1, t1, t2 	# 2y + C
	sub	t0, t0, t1	# 4x - (2y + C)
	
	add	a0, zero, t0
    	jr ra
    
