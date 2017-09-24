# Computer Architecture - Chapter 2 (MIPS instructions) (cont'd)

>2017/08/31
>
>Week 2, Lecture B

- [Computer Architecture - Chapter 2 (MIPS instructions) (cont'd)](#computer-architecture---chapter-2--mips-instructions---cont-d-)
  * [Instruction Formats](#instruction-formats)
  * [Instruction Categories](#instruction-categories)
  * [Integer Add/Subtract](#integer-add-subtract)
  * [Shift Operations](#shift-operations)
  * [Binary Multiplication](#binary-multiplication)
  * [I-Type Format](#i-type-format)

## Instruction Formats

- Register (R-type)
	- Register-to-register instructions
		- All data values used are located in registers
	- **Op**: op code
		- Specifies operation and format of instruction
	- **Rs, Rt**: first and second source operands
		- Read-enabled
	- **Rd**: destination operand
		- Write-enabled
	- **Sa**: shift amount used by shift instructions
	- **funct**: 6 bits for function code
		- Extends opcode
		- Up to 2^6 = 64 functions can be defined by same opcode
		- MIPS uses opcode 0 to define R-type instructions
	- ![](https://i.imgur.com/88mwj2X.png)
- Immediate (I-type)
	- Operates on an immediate value and a register value
		- Immediate values are max of 16 bits
	- ![](https://i.imgur.com/CSnxU58.png)
- Jump (J-type)
	- Used by jump instructions
	- ![](https://i.imgur.com/56USBCM.png)

![Table](https://i.imgur.com/LlJPFNP.png)

## Instruction Categories

- Arithmetic/Logical
	- Includes shift
- Data Transfer
	- Load/store
- Jump/branch
	- Flow control
- Floating point Arithmetic
- Misc.
	- Controls exception handlers
	- Mem. mgmt.

## Integer Add/Subtract

- `add`, `sub`
	- Overflow causes exception
	- `addu`, `subu` allows over

## Shift Operations

- Constant amounts
	- `sll`, `srl`: shift left/right by constant amount (sa)
	- `sra`: shift right arithmetic by constant amount
	- `l` stands for 'logic'
- Variable amounts
	- `sllv`, `srlv`, `srav`
		- Same as constant versions, but register used instead of sa for shift amount

![](https://i.imgur.com/rZrZVcU.png)

- Examples:
	- Assume `$s2 = 0xabcd1234`, `$s3 = 16`
	- `sll    $s1, $s2, 8    $s1 = $s2<<8    $s1 = 0xcd123400`
	- `sra    $s1, $s2, 4    $s1 = $s2>>4    $s1 = 0xfabcd123`
	- `srlv    $s1, $s2, $s3    $s1 = $s2>>$s3    $s1 = 0x0000abcd`

## Binary Multiplication

- `sll`: multiply by two by shifting left
- For more complex multiplication, factor into powers of 2
	- Ex: multiply by 36
		- 36 = (4 + 32), use distributive property
	- Ex: multiply by 26
		- 26 = (2+8+16)
			- 2: shift by one bit
			- 8: shift by three
			- 16: shift by four
		```asm
		sll $t0, $s1, 1        ; $t0 = $s1 * 2
		sll $t1, $s1, 3        ; $t1 = $s1 * 8
		addu $s2, $t0, $t1     ; $s2 = $s1 * 10
		sll $t0, $s1, 4        ; $t0 = $s1 * 16
		addu $s2, $s2, $t0     ; $s2 = $s1 * 26
		```

## I-Type Format

![](https://i.imgur.com/UP1FqBw.png)

- 16-bit constant stored in instruction
	- Rs is source register
	- Rt is now **destination** register (was Rd in R-type)
- Examples:
	- Add immediate: `addi $s1, $s2, 5    ; $s1 = $s2 + 5`
	- OR immediate: `ori $s1, $s2, 5    ; $s1 = $s2 | 5`
- `addi`: overflow -> exception
	- `addiu` allows overflow
- Immediate constant for `addi`, `subi` is **signed**
	- Therefore, no need for `subi`, `subiu`
- Immediate constant for `andi`, `ori`, `xori` is **unsigned**
