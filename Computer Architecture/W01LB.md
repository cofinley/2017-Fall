
# Computer Architecture - Chapter 1 Continued

> 2017/08/24
>
> Week 01, Lecture B

<!-- TOC -->

- [Memory Addressing](#memory-addressing)
- [Byte Ordering](#byte-ordering)
- [Types and Sizes of Operands](#types-and-sizes-of-operands)
- [Operations](#operations)
- [Control Flow Instructions](#control-flow-instructions)
- [Procedure Calling Conventions](#procedure-calling-conventions)
- [Encoding an Instruction Set](#encoding-an-instruction-set)
- [Response Time & Throughput](#response-time--throughput)
- [Definition of Performance](#definition-of-performance)
	- [Execution time](#execution-time)
	- [Clock Cycles per Instruction (CPI)](#clock-cycles-per-instruction-cpi)
		- [Performance Equation](#performance-equation)
		- [Example](#example)

<!-- /TOC -->

## Memory Addressing

- How to specify and interpret memory address is important since all dad is initially in memory
- Interpreting memory address
- Alignment of bytes
	- Memory aligned by word or double-word boundaries
	- Misalignment = extra memory access = hardware costs

## Byte Ordering

- Ordering bytes within a word in two ways
- Little Endian
    - Memory address = address of least significant byte
    - Small -> big
- Big Endian
    - Memory address: address of most significant byte
    - Big -> small
- Can be a problem with data exchange b/w computers with different endianess
- No benefit to using one over the other

## Types and Sizes of Operands

- Char: 8-bit, usually in ASCII
- 16-bit unicode: used in Java
- Integers: almost univesally represented as two's complement bin numbers
- Single precision: ...

## Operations

- Arithtmetic
- Data transfer
- Control
- System
- Floating point
- Decimal
- String
- Graphics

## Control Flow Instructions

- Four types:
    1. Branches (conditional)
    2. Jumps (unconditional)
    3. Procedure calls
    4. Procedure returns
- Control flow addressing modes:
    - Often PC-relave (PC + displacement)
        -  Target near current instruction
        -  Relative position = less bits
        -  Relocatable
    -  Register indirect jumps (register has address)
        -  Procedure returns

## Procedure Calling Conventions

- Two major conventions:
    1. Caller saves
        - Before call, procedure caller saves registers that will be need later, even if never used by callee
    2. Callee saves
        - Inside call, called procedure saves registers that it will overwrite
        - Can be more efficient if many small procedures
        - Better to use temporary storage
- Combination of both used commonly used
    - I.e. MIPS

## Encoding an Instruction Set

- Variable
    - Supports any number of operands
    - Each address specifier determines the addressing mode and length of specifier for operand
    - Allows for smallest code
- Fixed
    - Always same number of operands
    - Addressing mode specified as part of opcode
    - Largest code
- Hybrid
    - Opcode specifies instruction formats
    - Add one or two fields to specify the addressing mode and one or two fields to specify operand fields

## Response Time & Throughput

- **Response time**
    - Time bw start and completion of task (from end user perspective)
    - CPU Time + Wait time (I/O, OS scheduling, etc.)
    - Aka execution time
- **Throughput**
    - Number of tasks machine can run in given period of time
    - Increasing throughput can improve response time
    - Decreasing execution time improves throughput

## Definition of Performance

$$\text{Performance}_x = \frac{1}{\text{Execution time}_x}$$

- 'X is $n$ times faster than Y'

$$\frac{Performance_X}{Performance_Y} = \frac{\text{Execution time}_Y}{\text{Execution time}_X} = n$$

### Execution time

- Real elapsed time
    - Wait time, IO, disk access, OS scheduling
    - Useful, but not good for comparison
- Our focus: **CPU Execution time**
    - Time spent executing instructions
    - Doesn't count I/O or OS time
    - Measured in seconds or **number of CPU clock cycles**
        - Clock cycle = Clock period = 1 / clock rate
        - Clock rate = freq = cycles/second
        - 1 Hz = 1 cycle/sec
        - 1 MHz = 10^6 cycles/sec
        - 1 GHz = 10^9 cycles/sec
    - CPU cycles * cycle time = CPU cycles / clock frequency
    - Maximize by reducing cycles required by program or increase clock frequency
- Example:
	- Program runs in 10 seconds on computer *X* with 2 GHz clock
	- What's the number of CPU cycles on computer *X*?
		- $X = 10$ sec $\times 2 \times 10^9$ cycles/sec = $20 \times 10^9$ cycles or 20 gigacycles
	- We want computer *Y* to run same program in 6 seconds
		- But *Y* requires 10% more cycles (110%) to run program
		- What's the clock rate for *Y*?
		- Y cycles = $1.1 \times 20 \times 10^9 = 22 \times 10^9$ cycles
		- Y clock rate = $22 \times 10^9$ cycles / $6$ sec = $3.67$ GHz

### Clock Cycles per Instruction (CPI)

- Instructions takes diff number of cycles to exec
    - Mult takes more time than addition
    - Floating point takes longer than integer
    - Mem access takes more time than registers
- **Average number** of clock cycles per instruction

#### Performance Equation

- CPU cycles = instruction count * CPI
- CPU Time = CPU cycles * cycle tme
    - = instruction count * CPI * cycle time
    - = (instruction count * CPI ) / clock frequency
- CPI = CPU cycles / instruction count

#### Example

- Machine A clock cycle time = 250 ps and CPI of 2.0
- Machine B clock cycle time = 500 ps and CPI of 1.2
- Which machine is faster, by how much?

>

- CPU exec time (A) = $250 \times 2 = 500$ ps
- CPU exec time (B) = $500 \times 1.2 = 600$ ps
- A has less execution time by 100 ps or 1.2x faster
