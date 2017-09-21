# Computer Architecture - Chapter 2 (cont'd)

> 2017/09/19
>
> Week 05, Lecture A



## System Calls

- MIPS has special `syscall` instruction
    - Obtain services from OS
        1. Load service number in reg. `$v0`
        1. Load args in regs `$a0`, `$a1`
        1. Issue `syscall` instruction
        1. Retrieve return vals from result reg
- Usage examples in slides
## Procedures

- AKA function
- Call and return
    - Put parameters in place where procedure can access
        - Arg regs: `$a0` through `$a3`
    - Transfer control to procedure and save return addr
        - Jump-and link instr.: `jal` (return addr saved in `$ra`)
    - Perform tasks
    - Put results in place where procedure can access
        - Two value regs to return results `$v0, $v1`
    - Return to claling procedure: `jr $ra` (jump to return addr)

### Procedure Instructions

- JAL (jump and link) used as call instruction
    - Save return addr in `$ra` and jump to proc
    - Tegister `$ra = $31` used by `JAL` as return addr
- JR (jump register) used to return from proc
    - Jump to instr whose addr is in reg `$ra (PC = $ra)`

### Procedure Example

- `swap` (in C)

```c
void swap (int v[], int k) 
{
    int temp;
    temp = v[k];
    v[k] = v[k+1];
    v[k+1] = temp;
}
```

- Params:
    - $a0 = addr of v[]
    - $a1 = k
    - Return addr is in $ra

- `swap` in MIPS assembly

```asm
swap:
    sll $t0, $a1, 2         # $t0=k*4, 4=word size
    add $t0, $t0, $a0       # $t0=v+k*4
    lw $t1, 0 ($t0)         # $t1=v[k]
    lw $t2, 4 ($t0)         # $t2=v[k+1]
    sw $t2, 0 ($t0)         # v[k]=$t2
    sw $t1, 4 ($t0)         # v[k+1]=$t1
    jr $ra                  # return
```

### Call/Return Sequence

- Suppose proc 'swap' as `swap(a, 10)`
    - Pass addr of `a` and `10` as args
    - Call swap saving return addr in `$31 = $ra`
    - Exec `swap` procedure
    - Return control to point of origin (return addr)

### Procedure Call Convention

1. Pass args
    - First used $a0-$a3, push on to stack if more args
1. Save registsers $a0-$a3 and $t0-$t9 if needed
    - Saved by caller
        - Just in case needed later
1. Exec JAL instruction

- Called procedure (callee) does this to setup stack frame:
1. Allocate memory for stack frame
1. Save callee-saved regs in stack frame
1. Update $sp and $fp

## Memory Layout

- Text: code
- Static data: global vars/pointers
- Dynamic data: **heap**
    - `alloc` in C
- Stack: automatic storage

### Stack Frames

- AKA proc call frame
- Block of memory   
    - Holds values passed to proc as args
    - Saves regs that a proc might modify but the proc's caller doesn't want changed
    - Provides space for vars local to proc
- Frames pushed and popped onto/from stack by adjusting:
    - Stack pointer `$sp = $29` and frame pointer `$fp = 30`
    - Decrement `$sp` to allocatie stack frame and increment to free


---

- Know addressing modes for different instruction types
    - I.e. pseudo-direct for jump
- Review load immediate (li) and load address (la) instructions