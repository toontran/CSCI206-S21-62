.text

.globl add_second



add_second:
    li t2, 60               # Max minutes & secs
    li t3, 24               # Max hours

	lw t0, 0(a0)			# Second
    addi t0, t0, 1
    beq t0, t2, else_min
    sw t0, 0(a0)
    jr ra

else_min:
    li t0, 0
    sw t0, 0(a0)            # Second = 0
    addi a0, a0, 4          # Minute
    lw t1, 0(a0)
    addi t1, t1, 1
    beq t1, t2, else_hour
    sw t1, 0(a0)
    jr ra

else_hour:
    li t1, 0
    sw t1, 0(a0)
    addi a0, a0, 4          # Minute = 0
    lw t4, 0(a0)            # Hour
    addi t4, t4, 1
    beq t4, t3, else_newday
    sw t4, 0(a0)
    jr ra

else_newday:
    li t4, 0
    sw t4, 0(a0)
    jr ra    
   
