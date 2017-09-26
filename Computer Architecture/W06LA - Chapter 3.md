# Computer Arch. - Chapter 3

> 2017/09/26
>
> Test next thursday
>
> Look at final project, content covered in chapter 4 
>
> **Exam questions will be like hw questions**

<!-- vim-markdown-toc GFM -->
* [Assemblers](#assemblers)
	* [Object File Format](#object-file-format)
	* [Additional Facilities](#additional-facilities)
	* [Loading](#loading)
* [Dynamic Linked Libraries (DLLs)](#dynamic-linked-libraries-dlls)
* [Arithmetic for Computers](#arithmetic-for-computers)
	* [Integer Addition](#integer-addition)
	* [Integer Subtraction](#integer-subtraction)
	* [Overflow](#overflow)
	* [Unsigned Integer Multiplication](#unsigned-integer-multiplication)
		* [Sequential Unsigned Multiplication](#sequential-unsigned-multiplication)
	* [Signed Integer Multiplication](#signed-integer-multiplication)

<!-- vim-markdown-toc -->

## Assemblers

- Converts assembly to binary machine instructions
	1. Create symbol table: map labels to memory addresses
	2. Translate assembly statement (op code, reg specifiers, labels) into binary
- Produces object file
	- Contains machine instructions, data, bookkeeping info

### Object File Format

- Six sections
	- Header: size and position of other pieces of file
	- Text segment: machine language code for routines
	- Data segment: binary representation of init'd data used by program
	- Relocation info: identifies instructions and data words that depend on absolute addresses when program loaded into memory
	- Symbol table: assoc addresses with external labels in source files, lists unresolved refs
	- Debugging info: contains short description of compilation method

### Additional Facilities

- Macro
	- Helps with frequently used instruction sequences
	- Differs from subroutines:
		- Macro replaced by sequence body on assembly
		- Macros don't cause subroutine call
		- Macros permit programmer to create/name for the abstraction
	- Create with `.macro macro_func($arg)`
		- Call with `macro_func($7)`, $7 can be anything

### Loading

- Before running program, it resides in a file
- OS brings file into memory and starts running
1. Read executable file header to determine size/text/data
1. Allocate memory space big enough for text/data segments
1. ...

## Dynamic Linked Libraries (DLLs)

- ...
- Lazy linkage
	- First run, linker resolves the program routine
	- Subsequent runs, defer to DLL, which knows what to do since it knows what to do
	- Kind of like caching

## Arithmetic for Computers

### Integer Addition

- Overflow if result out of range
- Adding positive and negative operands, no overflow
- Adding to positive operands
	-overflow if result sign is 1
- Adding two negative operands
	- ...

### Integer Subtraction

- Add negation of second operand
- ...

### Overflow

- Use MIPS `addu`, `suu`, `addui`
- Raise exceptions with `add`, `addi`, `sub`
	- On overflow, handle exception (invoke handler)
		- Save PC in **exception program counter (EPC)** register
		- Jump to handler address
		- mfc0 (move from coprocessor reg) instruction can retrieve EPC value, to return after corrective action

### Unsigned Integer Multiplication

- 1100 * 1101 = 10011100 = 156
- Show slide
- 0 * multiplicand = 0
- 1 * multiplicand = multiplicand
- **m-bit multiplicand \* n-bit multiplier = (m+n)-bit product**
- Done via shifting and addition

#### Sequential Unsigned Multiplication

1. Init product = 0
1. Check each bit of multiplier
1. If multiplier bit = 1 then product = product + multiplicand
1. Shifting multiplicand to left
1. Repeat steps 3 & 4

### Signed Integer Multiplication

- One way:
	- Convert multiplier to multiplicand into positive numbers
		- If negative, then get 2's complement and remember sign
	- Perform unsigned multiplication
	- Compute sign of product
	- If product sign less than 0, then get 2s complement of product
- Other way:
	- ...

