

# Operating Systems - OS Structures

> 2017/08/24
>
> Week 01, lecture B

<!-- TOC -->

- [Services](#services)
- [Functions](#functions)
- [System Calls](#system-calls)
	- [Implementation](#implementation)
	- [System Call Parameter Passing](#system-call-parameter-passing)
	- [Types of System Calls](#types-of-system-calls)
		- [Examples of Windows and Unix System Calls](#examples-of-windows-and-unix-system-calls)
- [System Programs](#system-programs)
- [OS Design & Implementation](#os-design--implementation)
	- [Structure Types](#structure-types)
		- [MS-DOS (simple)](#ms-dos-simple)
		- [Unix (more complex)](#unix-more-complex)
		- [Layered](#layered)
		- [Microkernel](#microkernel)
		- [Modular](#modular)
		- [Hybrid](#hybrid)
- [Virtual Machines](#virtual-machines)
- [OS Debugging](#os-debugging)

<!-- /TOC -->

## Services

- UI
	- CLI
		- Doesn't use kernel but uses system-call interface to develop the command line interpreter
	- GUI
	- Batch
- Program Execution
	- Allow user to easily run programs without worrying about memory allocation, multitasking, etc.
- I/O
	- Abstract details of I/O for user
- File system changes
- Communications
	- Within same computer or network
	- Possibly through shared memory or message passing
- Error detection
	- Could occur anywhere
		- CPU
		- Memory
		- I/O
	- OS needs to be aware of possible errors

## Functions

- Resource allocation
	- Handle multiple users and simultaneous processes
	- CPU cycles, main memory, storage, I/O
- Accouting of users and spent resources
- Protection & Security
	- Handle owners/roles in multi-user environment or network
	- Protection: access control for resources
	- Security: resist outsiders through authentication and defend against invalid access attempts

## System Calls

- Programming interface of an OS
	- How programs request service from kernel
- Usually written in high-level language like C or C++
- Accessed by programs via **API** rather than direct system call use
	- API handled by **system call interface**
	- API abstracts the system call to the user one level higher than system call
	- Better for program **portability**
	- Uses system call lookup table
		- System call interface intercepts function calls in the API (user mode) and invokes the necessary system calls in the OS (kernel mode)
		- E.g. API -> system call interface -> system call
- Most common: Win32 API, POSIX API (Unix, Linux, Max OS X), Java API (JVM)

### Implementation

- Called doesn't need to know how system call implemented
	- Just need to obey API
- API allows for better portability

### System Call Parameter Passing

- Three methods to pas params to OS
	1. Simplest: pass params to registers
		- Fast, but limited size
	2. Parameters stored in block/table in memory, address of block passed as param to register
		- Found in Linux, Solaris
	3. Parameters pushed onto stack by program, popped by OS

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
	- Control resource access
	- Get/set permissions
	- Allow/deny user access

#### Examples of Windows and Unix System Calls

![](https://i.imgur.com/3RwdLDP.png)

## System Programs

- Types:
	- File mgmt.
	- Status info
	- File mod. (text editor, file search)
	- Programming language support (compilers, linkers, interpreters)
	- Program loading and exec (loaders)
	- Comms (virtual links, messaging)
	- Applications (web browser, office suite)
- User deals with system programs, not system calls usually

## OS Design & Implementation

- Goals
	- **User**: OS should be simple to learn and use, reliable, safe, fast
	- **System**: OS should be easy to design, implement, maintain, be flexible, reliable, efficient, error-free
- Principles:
	- **Policy**: What will be done?
	- **Mechanism**: How to do it?

### Structure Types

#### MS-DOS (simple)

- Written to provide most functionality in least space
	- No separation of modules
	- Single-tasking systems
	- Simple method to run program
		- No process created
		- Program loaded into memory, overwrites all but kernel
	- Shell started on boot
		- Reloaded on program exit
	- Single memory space

#### Unix (more complex)

- Limited by hw
- Two parts
	- System programs
	- Kernel
		- Everything below system call interface and above physical hardware
			- File system, CPU scheduling, mem. mgmt., etc. A lot for one half.
- Example: Unix/Linux

#### Layered

- Levels/layers of OS
	- Bottom: hardware
	- Top: UI
	- Each layer only builds off lower layers, not upper
- Advantages: abstraction and better debugging (assuming lower levels are working properly)
- Example: Windows 2000

![](https://i.imgur.com/Hq3HPMh.png)

#### Microkernel

- Moves as much from kernel to user space
- Benefits:
	- Easier to extend microkernel
	- Easy to port OS to new architectures
	- Reliable (less code running in kernel mode)
	- Secure
- Detriments:
	- Performance
		- Communication overhead between user and kernel space
- Example: Amiga OS

#### Modular

- OS implements **loadable kernel modules**
- Popular design
- OOD
	- Communication through common interfaces
- Core components all separate
	- Loaded by kernel as needed
- Similar to layered, but more flexibility
- Examples: Linux, Solaris

![](https://i.imgur.com/RsRuvDK.png)

#### Hybrid

- Most OS's are not just one design
- Combine approaches to get best balance of security, performance, usability
- Linux and Solaris are part monolithic, part modular
- Windows is mostly monolithic

---

- Quiz
	- How is modular approach similar/different to/from layered?
		- Similar to layered b/c each kernel section defined with protected interfaces, but more flexible because modules can call any other module

## Virtual Machines

- Layered approach
	- Treats hardware and OS kernel as all hardware
- Protected from host, host protected from virtual machine
- Requires good hardware support to better virtualize the exact underlying machine
- Good for **OS designer**: don't have to mess with actual machine when developing, easy to debug
- Good for **user**: don't have to worry about vm affecting actual machine

## OS Debugging

- Log files generated by OS
	- **Application** failure can generate **core dump** file capturing **process memory**
	- **OS** failure can generate **crash dump** file capturing **kernel memory**
- Performance tuning
	- Trace listings of activities are recorded
		- Used for profiling
