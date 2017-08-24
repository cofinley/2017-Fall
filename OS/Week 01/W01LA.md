# Operating Systems

> 2017/08/22
>
> Week 01, Lecture A

- OS is a colllection of programs that control the hardware
  - Kernel: program that is running all the time
	- OS runs processes in low-privilege state and provides service calls that invoke the kernel in high 
      - Allows computer hw to run efficiently

- Four components to a computer:
	1. HW
	2. OS
	3. Applications
	4. User

- Types of OS's:
	1. Single user (easy to use)
	2. Multi-user (mainframe) (maximizes resources util.)
	3. Dedicated system users (workstations) (usability balanced with resource utilization)
	4. Handheld (maximizes usability and battery life)

- Activities performed by OS:
	- Manage memory
	- Resource alloc.
	- UI
	- I/O mgmt.
	- Networking
	- Manage processing tasks
	- Manage file systems
	- Common hw functions

## Operation

- I/O and CPU operate concurrently
- Each device controller in charge of own device
	- Each also has own local buffer
- CPU moves data from/to main mem. to/from local buffers
- I/O is from device to locall buffer of controller
- Device cont. informs CPU that it has finished its op by causing an **interrupt**
	- Interrupt transfers control to the interrupt service routing through the **interrupt vector**, which contains the addresses of all the service routines
- A **trap** or **exception** is a software-generated interrupt caused by an error or user request
- OS's are **interrupt-driven**

## I/O Structure

- After I/O start, control returns to user program only after I/O completes
	- Wait instructures idles the CPU until next interrupt
	- Wait loop (contention for mem access)
	- At most one I/O request at a time, no simultaneous IO processing
- After I/O starts, control returns to user program without waiting for I/O completion
	- **System call**: request to OS to allow user to wait for I/O completion
	- **Device-status table**: contains entry for each IO device with its type, addr, and state

## Storage Structure

- Main mem
	- Only storage CPU can directly access
	- **Random access**
	- Usually **volatile**
- Secondary Storage (large, nonvolatile)
- Hard disk
	- Disk surface divided by **Tracks**, which are then divided by **sectors**
	- **Disk controller** determines the logical interaction bw the device and comp
- Solid State Disks
	- Faster than hard disks, non-volatile

### Storage Hierarchy

- Hierarchy
	- Speed
	- Cost
	- Volatility
- Caching
	- copying info into faster storage
- **Device driver** for each device controller to manage IO
	- Uniform interface b/w controller and kernel

![](https://i.imgur.com/zwF5cP5.png)

## Computer-System Arch

- Most systems: single general-purpose processor
- **Multiprocessors**: multiple processors
	- Aka **parallel systems, tightly coupled systems**
	- Each processor has its own registers and cache which share the main memory
	- Advantages:
		- Throughput
		- Economy of Scale
		- Reliability (fault tolerant)
	- Disadvantages:
		- More complex that single processor systems
	- Two types:
		1. **Asymmetric** multiprocessing: each processor assigned to one task
			- One master CPU and other slave CPUs
				- I/O usually reserved for master, tasks for slaves
		2. **Symmetric** multiprocessing: each processor performs all tasks
			- All processors equal, I/O and tasks performed on any CPU

### Dual-core design

- Multi-chip and **multicore**
	- Multicore is still one CPU

### Clustered Systems

- Like multiprocessors, but multiple systems working together instead of one system with multiple processors
- Usually shares storage via **storage-area network (SAN)**
- **High availability** which survives failures
	- **Asymmetric clustering**: one machine in hot-standby mode
	- **Symmetric clustering**: multiple nodes performing tasks and monitoring each other
- Sometime used for **high-performance computing (HPC)**
	- **Parallelization**
- Some have **distributed lock manager (DLM)** to avoid race conditions and conflicting ops

## Types of OS

### Batch OS

- Users don't interact with comp direclty, jobs prepared offline which are submitted to comp operator
- Problems:
	- Lack of interaction b/w user and job
	- CPU often idle
	- Difficult to provide priority

### Time-sharing

- Users use terminals to connect to same computer system at same time
- Logical extension of multiprogramming
- Advantages:
	- Quick response
	- Avoids software duplication
	- Less CPU idle time
- Disadvantages:
	- Reliability
	- Security of programs/data
	- Data communication

### Distributed

- Uses multiple central processors to serve multiple real-time apps and users, jobs are distributed among the processorss accordingly
- Advantages:
	- Resource sharing
	- Speedup of data exchange
	- Graceful failure of nodes
	- Better service to customers
	- Load reduction on host computer
	- Reduction of data processing delays

### Network

- Runs on networked server
- Allows shared files and printer access in a network (usually LAN)
- Advantages:
	- Centralized and therefore more stable
	- Security is managed by server
	- Upgrades are easier
	- Remote access possible
- Disadvantages:
	- Cost
	- Central location dependency
	- Regular maintenance

### Real-time

- Time interval required to process and responds to inputs is so small that it controls the env
- Two types:
	1. Hard real-time: guarantee that critical tasks complete on time, data stored in ROM, no virtual memory, usually
	2. Soft real-time: less restrictive, critical tasks get priority over others

## OS Ops

- **Interrupt driven** (hw and sw)
	- Hardware interrupt by one the devices
	- SOftware: **exception** or **trap**
		- Software error (division by zero)
		- Request for OS service
		- Infinite loop, processes modding other processes
- **Dual-mode**
	- Allows OS to protect itself
	- **User mode** and **kernel mode**
	- **Mode bit** provided by hw
		- Ability to discern b/w user code and kernel code
		- Some instructions are **privileged**, only executable in kernel mode
	- System call changes mode to kernel, return from call resets it to user

### Transition from User to Kernel Mode

- Timer to prvent inf. loop / process-hogging resources
	- Timer to to interrupt comp after some time
	- Counter decremented by system clock
	- OS sets counter (privileged instruction)
	- At 0, generate interrupt
	- Set up before scheduling process to regain control or terminate program that exceeds allotted time

## Process Mgmt.

- Each program is encapsulated in a process
	- Process includes complete execution (code, data, PC, registers, OS resources, etc.)
	- Five major activities for OS in process mgmt.:
		1. Creation/deletion of user and system processes
		2. Suspension and resumption of processes
		3. Mechanism for process synchronization
		4. "" process communication
		5. "" deadlock handling

## Memory Mgmt.

- Each word or byte has its own address
- Major activities of OS with memory mgmt.:
	- Track parts of memory in use
	- Decide which processes are loaded into memory when space is available
	- De/Allocate memory space as needed

## File Mgmt.

- Five major activities of an OS in file mgmt.:
	1. File creation/deletion
	2. Directory creation/deletion
	3. Support of primitives for changing files/directories
	4. Mapping files onto secondary storage
	5. Backup of files to stable media

### Mass-Storage Mgmt.

- Three major activities:
	1. Managing of free space on secondary storage device
	2. Allocation of space when files need to be written
	3. Scheduling request for memory access

### Performance of Various Levels of Storage

![](https://i.imgur.com/AKrTjqV.png)

## Data Migration

- From hard disk to main memory to cache to register
- When multitasking, OS must be careful to choose most recent data value, no matter the location
	- Even more complex in distributed environment

## I/O Subsystem

- OS hides low-level features of hw from user
- Memory mgmt of IO
	- Buffering  (temp storage of data while being transferred)
	- Caching
	- Spooling (overlapping of output in one job vs. input of other jobs)
- Drivers for specific devices

## Protection & Security

- Protection
	- Sandbox processes running simultaneously between users/environments
- Security
	- Defense against DoS, worms, viruses, theft

## Kernel Data Structures

- Singly linked list
- Doubly linked
- Circularly linked
- BST
- Hash Map
- Bitmap
	- String of *n* binary digits representing the status of *n* items

## Computing Environments

- Portals (web access to systems)
- Network computers (**thin clients**) (web terminals)
- Mobile computers on wireless networks

### Distributed Computing

- Collection of systems networked together
	- Network could be:
		- LAN
		- WAN (internet)
		- Metropolitan Area Network (MAN)
		- Personal Area Network (PAN)
	- A network OS can provide features across network
		- Illusion of single system

### Client/Server

- Dumb terminals that connect to smart PCs
- Compute-server
	- Requests services (i.e. database)
- File-server
	- Request files

### Peer-to-peer

- Another model of distributed
- Does not distinguish clients and servers
	- All nodes are peers and servers
	- Node must join network
		- Register name with central lookup service _or_
		- Broadcast request & respond to requests for service via **discovery protocol**

### Virtualization

- Guest OS within host OS
- All natively compiled

### Cloud Computing

- Computing, storage, apps across network
- Extension of virtualization
- Types:
	- Public cloud: available via internet for anyone
	- Private cloud: run by company for company
	- Hybrid cloud: both public and private
	- Software as a Service (SaaS)
		- 1+ applications via internet (i.e. Google Docs)
	- Platform as a Service (PaaS)
		- Software stack ready for applicatin use via internet (i.e. database server)