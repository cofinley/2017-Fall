.data

str1: .asciiz "Enter a string of at most 100 characters: "

input_str: .space 100

.text

main:

### Prompt ###

la $a0, str1		# load str1 address into $a0
li $v0, 4		# load I/O code for string output
syscall			# output str1

### Input sentence ###

la $a0, input_str	# input sentence
li $a1, 100
li $v0, 8
syscall


### Iterate ###

la $t0, input_str	# load address of sentence
li $t1, 0		# basic char counter. use to computer total string length

countChr:
lb $t2, 0($t0)  	# Load the first byte from address in $t0  
beqz $t2, end   	# if $t2 == 0 then go to label end  
add $t0, $t0, 1      	# else increment the address  
add $t1, $t1, 1 	# and increment the counter
j countChr
   
end:

li $v0, 1		# print final length (includes null terminator)
move $a0, $t1
syscall