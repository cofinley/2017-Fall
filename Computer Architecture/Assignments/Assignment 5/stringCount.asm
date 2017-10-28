.data

str1: .asciiz "\nEnter a string of at most 100 characters: "
str2: .asciiz "\nEnter a character: "
str4: .asciiz "\nEnter a string of two characters: "
str3: .asciiz "\nNumber of occurrences of "
equalsign: .asciiz " = "
str5: .asciiz "\nRepeat (y/n)? "

input_str: .space 101
single_char: .space 1
double_char: .space 2


.text

main:

### Sentence Prompt ###

la $a0, str1           	# load str1 address into $a0
li $v0, 4              	# load I/O code for string output
syscall               	# output str1

### Input sentence ###

la $a0, input_str	# input sentence
li $a1, 100
li $v0, 8
syscall

move $t0, $a0		# Inputted sentence address
move $s0, $t0		# Save address for secondary use later

### Char Prompt ###

la $a0, str2           	# load str1 address into $a0
li $v0, 4              	# load I/O code for string output
syscall               	# output str1

### Input char ###

la $a0, single_char	# input char
li $a1, 2
li $v0, 8
syscall

move $t1, $a0		# Inputted single char address


### Iterate ###

lb $t5, 0($t1)		# Get inputtted single char from address
li $t2, 0    		# Char occurrence counter

countChr:
lb $t3, 0($t0)  	# Load the first byte from address in $t0 (inputted sentence)
beqz $t3, end1  	# if $t3 == 0 then end of string; go to label 'end'
seq $t4, $t5, $t3	# If chars equal, set $t4 = 1, else $t4 = 0
add $t0, $t0, 1      	# else increment the address
add $t2, $t2, $t4 	# and increment the counter if chars equal
j countChr
   
end1:

la $a0, str3		# Print out "number of occurrences" string
li $v0, 4
syscall

la $a0, 0($t1)		# Print out single char
li $v0, 4
syscall

la $a0, equalsign	# Print out equal sign
li $v0, 4
syscall

li $v0, 1		# Print counter's result
move $a0, $t2
syscall


### Char Prompt ###

la $a0, str4           	# load str1 address into $a0
li $v0, 4              	# load I/O code for string output
syscall               	# output str4

### Input two-char string ###

move $t0, $s0		# Retrieve original sentence address

la $a0, double_char	# input char
li $a1, 3
li $v0, 8
syscall

move $t1, $a0		# Inputted single char address

### Iterate ###

lb $s0, 0($t1)		# Get first of two inputtted chars from address
lb $s1, 1($t1)		# Get second of two inputtted chars from address

li $t2, 0		# Two-char occurrence counter
li $t5, 0		# marker 1 (first char match)
li $t6, 0		# marker 2 (second char match)

count2Chr:
lb $t3, 0($t0)  	# Load the first byte from address in $t0 (inputted sentence)
beqz $t3, end2  	# if $t3 == 0 then end of string; go to label 'end'

seq $t6, $s1, $t3	# If second char equal, set marker 2 to true, else false
and $t7, $t5, $t6	# AND the two markers
add $t2, $t2, $t7 	# Use AND result to increment the counter if two-char string match

move $t5, $zero		# No two-char match, reset both markers
move $t6, $zero

seq $t5, $s0, $t3	# If first char equal, set marker 1 to true, else false
add $t0, $t0, 1      	# Increment the address
j count2Chr

end2:

la $a0, str3		# Print out "number of occurrences" string
li $v0, 4
syscall

la $a0, 0($t1)		# Print first of double-char string
li $v0, 4
syscall

#la $a0, 1($t1)		# Print second of double-char string
#li $v0, 4
#syscall

la $a0, equalsign	# Print out equal sign
li $v0, 4
syscall

li $v0, 1		# Print counter's result
move $a0, $t2
syscall