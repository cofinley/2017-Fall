# Operating Systems - Processes

> Chapter 3
>
> 2017/08/29
>
> Week 2, Lecture A

- [Operating Systems - Processes](#operating-systems---processes)
  * [Process](#process)
    + [State](#state)
      - [State Transitions](#state-transitions)
      - [State Components](#state-components)
  * [Process Control Block](#process-control-block)
  * [Context Switching](#context-switching)
  * [Process Scheduling](#process-scheduling)
  * [Schedulers](#schedulers)
  * [Process Operations](#process-operations)
    + [Creation](#creation)
    + [Termination](#termination)

## Process

- Program in execution, async task/job
- Not same as program
	- Program is only part of the process
	- Process: **active**
	- Program: **passive**
- Process memory divided in four sections:
	- Text
		- Code
	- Stack
		- Temp data
			- Func params, return addrs, local variables
	- Data
		- Global variables
	- Heap
		- Memory dynamically created at run time
	- Stack and heap can grown in memory

### State

- New state: process created
- Running: CPU being used by process
- Blocked/Waiting: I/O completion needed
- Ready: process ready, but waiting for other process
- Terminated: process finished execution

![](https://i.imgur.com/13aZmRm.png)

#### State Transitions

- Transition one: process discovers it can't continue
	- Running -> Blocked
- Transition 2: scheduler decides that running process has run long enough, let other process have a turn
	- Running -> Ready
- Transition 3: all other processes have had their turn, time for first process to run again
	- Ready -> Running
- Transition 4: external event occurs which allows process to continue
	- Blocked -> Ready
- Transition 5: process created
	- New -> Ready
- Transition 6: finished executing
	- Running -> Terminated

---

Quiz: **how many interrupts will be created?**

```c
main(){
	product =1;    
	k = 0;    
	sum =0;     
	while (k<100){
		product = product * k;
		k++;
		print (product);
		sum = sum + product + k;
		print(sum);      
	}  
}
```

- Answer: **200**
	- Each time print function runs, this requires an interrupt to print to I/O device

#### State Components

- Program data (static and dynamic)
- Program procedure call stack
- General purpose registers' contents

## Process Control Block

- Data structure
- "PCB"
- Defines process to OS
- Contains info about process
	- Current state
	- UID
	- Pointer to parent and child process
	- CPU scheduling info
	- Pointers to program memory
	- Register save area
	- Processor being used
	- Accounting info
	- I/O status

## Context Switching

- Process of saving the state of the current process and loading the latest state of the new process
- Switching time is all overhead
	- OS can't do much during
	- Time depends on memory speed, register saving speed, # of registers

## Process Scheduling

- Criteria
	- Maximize
		- CPU util (want CPU to work all the time, limit idling)
		- Throughput  (# of processes at a time)
	- Minimize
		- Wait time (time spent in ready queue)
		- Response time
- Affects time process spends in ready queue
- **Process scheduler** handles which process will go next in execution
	- Maintains **scheduling queues**
		- **Job queue**: all processes
		- **Ready queue**: processes in main memory, ready, waiting for execution
		- **Device queue**: processes waiting for I/O

## Schedulers

- Short-term scheduler (CPU scheduler)
	- Selects process to be executed next
	- Invoked frequently
- Long-term scheduler (job scheduler)
	- Selects processes to bring into ready queue
	- Invoked infrequently
	- Controls degree of **multiprogramming**
- Processes are either
	- **I/O-bound**: spends more time doing IO than computation, many short CPU bursts
	- **CPU-bound**: more time doing computations, few long CPU bursts
	- Strive for a mix of the two in long-term scheduler
- Medium-term scheduler
	- Added if degree of multiprogramming needs to decrease
	- Push from memory to disk
		- Use swapping to bring back and forth for execution

## Process Operations

### Creation

- On startup, system call, or user request
- Parent creates child processes (tree)
	- Can divvy up resource sharing and executing options
- Examples: 
	- `fork()`: new child process
	- `exec()`, `execlp()`: after fork, replace process' memory space with new program
	- `wait()`:  parent waits for child process to complete
		- Takes pointer to int, returns PID of completed process
			- If no child, return -1
		- Wait for an unspecified child process:
			- `wait(&status);`
		- Wait for a specific child process whose ID is known:
			- `while (pid != wait(&status)){}`

```c
int main() {
	pid_t pid;

	pid = fork();
	
	if (pid < 0) { /* error */
		return 1;
	}
	else if (pid == 0) { /* child process */
		execlp("bin/ls", "ls", NULL);
	}
	else  { /* parent process */
		wait(NULL);
		printf("Child complete");
	}
	return 0;
}
```

```c
void main(void)
{
	pid_t pid, pid_child;
	int status;
	 
	if ((pid = fork()) == 0) {
		// child here
		child();
	}
	else { 
		// parent here
		parent();
		pid_child = wait(&status);
	}
}
```

### Termination

- When process done, error occurs, fatal error occurs, or killed by other process
- Examples:
	- `exit()`: process deleted, resources reallocated
	- `abort()`: parent terminates child process
- Some OS's don't allow children to live without parents
	- If so, must terminate children and grandchildren when parent terminated
		- Cascading termination (recursive abort)
