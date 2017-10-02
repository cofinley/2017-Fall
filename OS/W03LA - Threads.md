# OS - Threads

- Process groups reseources together, threaj
- ...

## Threads

- Allow multiple streams of execution (parallelism)
- CPU switches b/w threads rapidly (illusion of parallelism)
	- Only one active at a time
- Like processes,
	- Thread can have same states as processes
		- Ready, running, blocked, terminated
		- Can create children threads
- Unlike processes,
	- Threads can access every address in task
	- Threads are not independent
		- They are designed to assist each other
- Consists of:
	- Program counter (PC)
	- Register set
	- Stack space
- Threads are great for:
	- Servers
		- Data shared, no need for IPC
		- Takes advantage of multiprocessors
	- Updating display
	- Fetching data (networking too)
- Threads not so good for sequential tasks
- Threads are cheap and fast but have no protection between them
	- Easy to create/destroy/switch context
	- Better for sharing than multi-processes, too

### Benefits

- Responsiveness
	- Execution still continues if part of process blocked 
- Resource sharing
- Economy
- Scalability

## Multicore Programming

- Challenges with multicore/multiprocessor
	- Balance, dividing activities, data splitting/dependency, testing/debug
- Parallelism - more than one task performed simultaneously
	- **Data**: splits data across multiple cores, same operation on each
	- **Task**: split threads across multiple cores, unique operation on each
- Concurrency - more than one task making progress
- Amdahl's Law

## Thread Levels

- **User threads**: mgmt. done by user-level thread lib
	- POSIX PThreads
	- Windows threads
	- Java threads
	- Threads only visible to process, only process visible to kernel
		- OS kernel doesn't see these threads
	- Advantages:
		- Can be implemented on OS with direct thread support
		- Doesn't modify OS
		- Simple representation and mgmt.
		- Fast/efficient
	- Disadvantage
		- No coop b/w OS
		- Required multi-threaded kernel, otherwise major blocking for process
- **Kernel threads**: kernel-supported
	- In all major OS's
	- Kernel sees threads directly
	- Advantages:
		- OS knows more about process and can prioritize those with more threads
		- Good for processes that frequently block
	- Disadvantages
		- Slow/inefficient (100's times slower that user-level)
		- Bigger/expensive overhead to be able to block each and every thread
			- Full thread control block (TCB)

## Multithreading Models

- Many-to-one
	- Many user-level threads mapped to one kernel-level thread
	- One block causes all to block
	- Uncommon
- One-to-one
	- Each user-level thread maps to kernel threads
	- More concurrency
	- Not great since each thread creation requires slow kernel threads
- Many-to-many
	- Many user level to many kernel threads
	- Only needs sufficient slower, kernel-level threads
	- Better efficiency, used often in major OS's
- Two-level
	- Like M-M, but allows user thread to be bound to kernel-level
	- Combines M-M and one-to-one

## Thread Libraries

- API for thread mgmt.
- Either in:
	- entirely user space
	- kernel-level supported by OS
