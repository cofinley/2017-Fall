# Operating Systems - Processing (cont'd)

> 2017/08/31
>
> Week 2, Lecture B

 * [Interprocess Communication (IPC)](#interprocess-communication--ipc-)
 * [IPC Models](#ipc-models)
   + [Shared memory](#shared-memory)
     - [Producer-Consumer Problem](#producer-consumer-problem)
   + [Message passing](#message-passing)
     - [Direct Communication](#direct-communication)
     - [Indirect Communication](#indirect-communication)
     - [Synchronization (buffering)](#synchronization--buffering-)
 * [IPC Examples](#ipc-examples)
   + [Posix shared memory:](#posix-shared-memory-)
   + [Mach (message passing)](#mach--message-passing-)
   + [Windows](#windows)
   + [Client-server systems](#client-server-systems)
     - [**Sockets**](#--sockets--)
     - [Remote Procedure Call (RPC)](#remote-procedure-call--rpc-)
     - [Pipes](#pipes)
       * [Types of Pipes](#types-of-pipes)
 * [Project 1 Info](#project-1-info)

## Interprocess Communication (IPC)

- Processes can talk with each other or be independent
	- Reasons to cooperate:
		- Information speedup
		- Performance speedup
		- Modularity
		- Convenience

## IPC Models

### Shared memory

- P1 store info in memory
- P2 load same info from memory
- Better for larger data
- Hurdle: synchronizing actions between multiple processes when accessing shared memory 

#### Producer-Consumer Problem

- **Unbounded-buffer** has no limit on size of buffer
- **Bounded buffer** assumes fixed buffer size
	- `#define BUFFER_SIZE 10`
	- Producer
		```c
		item next_produced; 
		while (true) { 
			/* produce an item in next_produced */ 
			while (((in + 1) % BUFFER_SIZE) == out) 
				; /* do nothing */ 
			buffer[in] = next_produced; 
			in = (in + 1) % BUFFER_SIZE; 
		```
	- Consumer
		```c
		item next_consumed; 
		while (true) {	while (in == out) 
				; /* do nothing */	next_consumed = buffer[out]; 
			out = (out + 1) % BUFFER_SIZE;
			/* consume the item in next consumed */ 
		} 
		```


### Message passing
	
- P1 sends info to kernel
- P2 receives same info from kernel
- Better for smaller communication
- Easier to implement
- Uses system call, therefore slower than memory access in shared memory approach
- Processes establish a **communication link**
	- Can have issues depending on implementation (e.g. how is link est., can the link span more than 2 processes, etc.)
	- Physical implementation: shared memory, hw bus, network
	- Logical: direct/indirect, sync/async, auto/explicit buffering

#### Direct Communication

- Processes communicate explicitly
	- Link assoc with only the one pair of processes
	- `send(P, message)`: send message to process P
	- `receive(Q, message)`: receive from process Q

#### Indirect Communication

- Messages sent/received to/from mailboxes (aka ports)
- Processes linked only if sharing common mailbox
- Can have multiple processes linked
- Processes can have multiple comm links
- `send(A, message)`: send message to mailbox A
- `receive(A, message)`: receive from A

#### Synchronization (buffering)

- Used in message passing
- Can be **blocking (synchronous)** or **non-blocking (async)**
	- Synchronous good b/c confirmation of receiving message, bad b/c of wasted time
		- If both sender and receiver blocking => **rendezvous** (syncs the two processes)
	- Async good b/c flow not restricted while waiting for response
		- Bad b/c buffering needs to handle multiple comms
			- Requires bigger implementation
- Queue/buffer of messages can be different capacity
	- Zero capacity: no messages queue on the link
		- Sender has to wait for receiver (rendezvous)
	- Bounded: finite length of messages
		- **Aka explicit buffering**
		- Send must wait if queue/buffer full
	- Unbounded: infinite length
		- **Aka automatic buffering**
		- Sender never waits

## IPC Examples

### Posix shared memory:

- Process creates shared memory segment
	- `id = shmget(IPC_PRIVATE, size, S_IRUSR|S_IWUSR);`
- Process wants access to that shared memory so it must attach to it
	- `shared_memory = (char *) shmat(id, NULL, 0);`
- Process can write to shared memory
	- `sprintf(shared_memory, "Writing to shared memory");`
- When done, process can detach shared memory from its address space
	- `shmdt(shared_memory);`
- Remove from system
	- `shmct1(segment_id, IPC_RMID,NULL)`

### Mach (message passing)

- System calls made by messages
	- `msg_send()`, `msg_receive()`, `msg_rpc()`
- Uses mailbox
	- Create via `port_allocate()`

### Windows

- Message passing via **advanced local procedure call (LPC)**
	- Uses ports
	- Client opens handle to port
	- Client send conn. req.
	- Serve creates 2 communication ports and returns one to client
	- Clien/server use port to send messages/callbacks and listen for replies

### Client-server systems

- Sockets
- Remote Procedure Calls
- Pipes
- Remote Method Invocation (Java)
	
#### **Sockets**

- Virtual connection endpoint
	- Communication occurs b/w pair of sockets
	- Bi-directional
- Format: `IP:port`
	- Ports below 1024 are well-known and used already for common services
- Code sample:
	- Create socket
		- `socketid = socket(AF_INET, SOCK_STREAM, DEFAULT_PROTOCOL);`
	- Connecting the socket
		- `status = connect(socketid, (struct sockaddr*)&serverINETaddress, server_len);`
	- Get message info
		- `status = write(socketid, buffer, len);`
	- Receive acknowledgement
		- `status =read(socketid, buffer, len);`
	- Cut the socket
		- `close(socketid)`

#### Remote Procedure Call (RPC)

- Abstracts procedure calls in networked system
- **Stubs**: client-side proxy for actual procedure on server
- Stub locates server and **marshalls** the parameters

#### Pipes

- Main comm in uniprocessor system
- Usually async send and sync receive
- Send/receive == "write"/"read"

##### Types of Pipes

- Ordinary
	- Used in producer-consumer style
		- Producer writes to the **write-end**
		- Consumer read from the **read-end**
	- Unidirectional
	- Requires parent-child relationship between processes
	- Aka **anonymous pipes**
- Named
	- More powerful, bidirectional
	- No parent-child relationship necessary
	- More processes can use pipe

---

## Project 1 Info

- Know types of communication in OS (message passing or shared memory), advantages/disadvanges, etc.
- If process id is 0, then it's child, if not, then parent
-  Header for project in slides
- Key
	- Best to generate yourself
		- `#define SHMKEY ((key_t) 1500)`
			- Make up number
	- To auto generate
		- `ftok`
- Shared memory
	```c
   typedef struct
   {
	   int value;
   } shared_memory;
   ```

- C4 Server: osnode[01-16].csee.usf.edu
