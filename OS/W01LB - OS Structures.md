
# Operating Systems

> 2017/08/24
>
> Week 01, lecture B

- [Operating Systems](#operating-systems)
    - [Services](#services)
    - [System Calls](#system-calls)
        - [Implementation](#implementation)
        - [System Call Parameter Passing](#system-call-parameter-passing)
        - [Types of System Calls](#types-of-system-calls)
            - [Examples of Windows and Unix System Calls](#examples-of-windows-and-unix-system-calls)
    - [OS Design & Implementation](#os-design-implementation)
        - [Structure Types](#structure-types)
    - [Virtual Machines](#virtual-machines)
    - [OS Debugging](#os-debugging)

## Services

- UI
    - CLI
        - Doesn't use kernel but uses system-call interface to develop the command line interpreter
    - GUI
- Program Execution
- File system changes
- Communications
    - Shared memory
- Error detection
    - CPU
    - Memory
    - I/O
- Resource alloc
- Accouting of users and spent resources

## System Calls

- Programming interface to OS services
- USually written in high-level language like C or C++
- Accessd by programes via API rather than direct system call use
    - API abstracts the system call to the user
    - Uses syscall lookup table
- Most common: Win32 API, POSIX API (Unix, Linux, Max OS X), Java API (JVM)

### Implementation

- Called doesn't need to know how syscall implements
    - Just need to obey API
- API allows for better portability

### System Call Parameter Passing

- Three methods to pas params to OS
    1. Simplest: pass params to registers
        - Fast, but limited size
    - ...

### Types of System Calls

- Process control
    - Load, exec, end, abort, create, get/set attrs, alloc
- File management
    - Create/delete/open/read/write
- Device management
    - Request/release device, read/write data, get/set attrs
- Information maintenance
    - Get/set time/date system data, attrs for process/file/device
- Communications
    - Create/delete connection, send/receive data, attach/detach devices
- Protection
    - ...

#### Examples of Windows and Unix System Calls

- Insert pic here

## OS Design & Implementation

- Principles:
    - Policy: What will be done?
    - Mechanism: How to do it?

### Structure Types

- MS-DOS (simple)
    - Written to provide most functionality in least space
        - No separation of modules
        - Single-tasking systems
        - Simple method to run task
- Unix (more complex)
    - Limited by hw
    - Two parts:
        - System programs
        - Kernel
            - Everything below syscall interface
- Layered
    - OS has levels/layers
        - Bottom: hw
        - Top: UI
        - Each layer only builds off lower layers, not upper
    - Advantages: abstraction and better debugging (assuming lower levels are working properly)
- Microkernel
    - Moves as much from kernel to user space
    - Benefits:
        - Easier to extend microkernel
        - Easy to port OS to new archs
    - Detriments:
        - Performance
- Modular
    - Loadable kernel modules
    - Popular design
    - OOD
    - Core components all separate
    - ...
- Hybrid
    - Most OSs are not just one design
    - ...
- Quiz
    - ...

## Virtual Machines

- Layered approach
    - Treats hw ...
- Protected from host, host protected from virtual machine
- Requires good hw support to better virtualize the exact underlying machine
- Good for OS designer: don't have to mess with actual machine when developing
- Good for user: don't have to worry about vm affecting actual machine

## OS Debugging

- Log files
- App failure can generate **core dump** file capturing memory of the process
- OS failure can generate **crash dump** file containing kernel memory
