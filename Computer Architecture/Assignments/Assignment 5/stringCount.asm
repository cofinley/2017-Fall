.data

str1: .asciiz "Enter a string of at most 100 characters: "
str2: .asciiz "Enter a character: "
str3: .asciiz "Number of occurrences of "
str4: .asciiz "Enter a string of two characters: "
str5: .asciiz "Repeat (y/n)? "
char: .asciiz "i"

input_str: .space 100
single_char: .space 4
double_char: .space 8


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

### Char Prompt ###

la $a0, str1           	# load str1 address into $a0
li $v0, 4              	# load I/O code for string output
syscall               	# output str1

### Input char ###

la $a0, single_char	# input sentence
li $a1, 3
li $v0, 8
syscall



### Iterate ###

la $t0, input_str  	# load address of sentence
li $t1, 0    		# basic char counter. use to computer total string length

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