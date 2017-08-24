# Computer Architecture

> 2017/08/24
>
> Week 01, Lecture B

## Memory Addressing

- How to specify and interpret memory addr is iportant since all dad is initially in memory
- Interpreting memory addr
    - ...

## Byte Ordering

- Ordering bytes within a word in two ways
- Little Endian
    - Memory addr = addr of least significant byte
    - Small -> big
- Big Endian
    - Mem addr: addr of most sig byte
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
    1. Jumps (unconditional)
    1. Procedure calls
    1. Procecure returns
- Control flow addressing modes:
    - Often PC-relave (PC + displacement)
        -  Target near current instruction
        -  Relative position = less bits
        -  Relocatable
    -  Register indirect jumps (register has addr)
        -  Procedure returns

## Procedure Calling Conventions

- Two major conventions:
    1. CAller saves
        - Before call, procedure caller saves registers that will be need later, even if never used by callee
    1. Callee saves
        - Inside call, called procedure saves registers that it will overwrite
        - Can be more efficient if many small procedures
        - Better to use temporary storage
- Combination of both used commonly used
    - I.e. MIPS

## Encoding an Instruction Set

- Variable
    - Supports any number of operands
    - Each addr specifier determines the addr mode and length of specifier for operand
    - Allows for smallest code
- Fixed
    - Always same number of operands
    - Addr mode specified as part of opcode
    - Largest code
- Hybrid
    - Opcode specifies instruction formats
    - Add one or two fieds to specify the addr mode and one or two fields to specify operand fields

## Response Time & Throughput

- Response time
    - Time bw start and completion of task (from end user perspective)
    - CPU Time + Wait time (I/O, OS scheduling, etc.)
    - Aka execution time
- Throughput
    - Number of tasks machine can run in given period of time
    - Increasing throughput can improve response time
    - Decreasing execution time improves throughput

## Definition of Performance

- Performance = 1 / Execution time
- 'X is *n* times faster than Y'
    - Perf_x/Perf_y = ExecutionTime_y/ExecutionTime_x = n

### Execution time

- Real elapsed time
    - Wait time, IO, disk access, OS scheduling
    - Useful, but not good for comparison
- Our focus: **CPU Execution time**
    - Time spent executing instructions
    - Doesnt count IO or OS time
    - Measured in seconds or **number of CPU clock cycles**
        - Clock cycle = Clock period = 1 / clock rate
        - Clock rate = freq = cycles/second
        - 1 Hz = 1 cycle/sec
        - 1 MHz = 10^6 cycles/sec
        - 1 GHz = 10^9 cycles/sec
    - CPU cycles * cycle time = CPU cycles / clock frequency
    - Maximize by reducing cycles required by program or increase clock frequency
- **Insert example questions here**

### Clock Cycles per Instruction (CPI)

- Instructions takes diff number of cycles to exec
    - Mult takes more time than addition
    - Floating point takes longer than integer
    - Mem access takes more time than registers
- **Average number** of clock cycles per instruction

#### Performance Equation

- CPU cyclces = instruction count * CPI
- CPU Time = CPU cycles * cycle tme
    - = instruction count * CPI * cycle time
    - = (instruction count * CPI ) / clock frequency

#### Example

- Machine A clock cycle time = 250 ps and CPI of 2.0
- MAchine B clock cycle time = 500 ps and CPI of 1.2
- Which machine is fater, by how much?

>

- CPU exec time (A) = 250 * 2 = 500 ps
- CPU exec time (B) = 500 * 1.2 = 600 ps
- A has less execution time by 100 ps or 1.2x faster