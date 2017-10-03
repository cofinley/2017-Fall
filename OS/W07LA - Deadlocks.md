# OS - Deadlocks

> 2017/10/3


<!-- vim-markdown-toc GFM -->
* [Deadlock Problem](#deadlock-problem)
	* [Bridge-Crossing Example](#bridge-crossing-example)
* [System Model](#system-model)
* [Conditions](#conditions)
* [Resource-Allocation Graph](#resource-allocation-graph)
* [Methods to Handle Deadlocks](#methods-to-handle-deadlocks)
	* [Prevention](#prevention)
	* [Avoidance](#avoidance)
		* [Banker's Algo](#bankers-algo)
	* [Deadlock Detection](#deadlock-detection)

<!-- vim-markdown-toc -->

## Deadlock Problem

- Set of blocked processes each holding a resource and waiting to acquire a resources held by another process in the set

### Bridge-Crossing Example

- One-way lane in middle of bridge
- Each section of bridge is resource
- If deadlock, one car can back up
- ...

## System Model

- Consists of resources
- Types:
	- CPU cycles, memory space, I/O
- To utilize:
	- request
	- use
	- ...

## Conditions

- For deadlock to occur, four conditions need to happen at the same time:
	- Mutex
	- Hold and wait
		- Proc holding 1+ resources is waiting to get addtl resources held by other processes
	- No preemption
		- Procs that can only be released voluntarily
	- Circular wait
		- Set of waiting procs ...

## Resource-Allocation Graph

- Vertices: two types
	- Set of all procs
	- Set of all resources
- Edges also two types:
	- ...

- Pic of graphs
- If no cycles, no deadlock
- If cycle,
	- If only one instance per resource type, deadlock
	- If several instances per resource type, possible deadlock

## Methods to Handle Deadlocks

1. Prevention, avoidance
1. Allow to enter deadlock, detect then recover
1. Ignore problem caused by deadlocks, pretend they never occur (used by most OS's, including UNIX)
	- Solution is to reboot/reset

### Prevention

- Restrict ways request can be made
	- Mutex: not req'd for sharable resources (read-only)
	- Hold and wait - must guarantee whenever proc requests resource, that it doesn't hold other resources
		- ...
	- No preemption
		- If proc that's holding reources requests another resource that can't be immediately alloc'd, then all resources held are released
		- Preempted resources are added to list of resources for which the proc is waiting
		- Proc will be reset only when it can regain its old resources, as well as new ones it's requesting
	- Circular wait
		- Impose total ordering of all resource types and require that each proc requests resources in inc. order
			- If at high number, small-numbered resource can't be allocated

### Avoidance

- Requires system to have *a priori* info available
- Simplest, most useful model requires each proc declare max number ...
- ...
- Safe state
	- ...
	- If system in safe state, no deadlocks
	- If in unsafe state, possible deadlock
- Algos:
	- Single instance of resource type: resource-alloc graph
	- Multiple instances of resources type: banker's algo

#### Banker's Algo

- Multiple resources instances
- Each proc must a priori claim max use
- When proc requests resource it may have to wait
- When proc gets all resources it must return them in a finite amount of time
- Let *n* = number of procs and *m* = number of types
	- **Available**: vector of length m
	- **Max**: n * m matrix
	- **Allocation**: n * m matrix
	- **Need**: n * m matrix, max - allocation
- Insert examples

### Deadlock Detection

- 2nd method to handle deadlocks
- Allow system to enter deadlock state
- Wait-for graph
	- ...
- Detection algo
	- Available: vector of length m = numbre of avail resources of each type
	- ...
	- How often to invoke depends on frequency of deadlocks
		- If invoked randomly, there might be many cycles in graph, and deadlock culprit may be unknown
- Recovery scheme
	- Terminate all deadlocked processes
	- Abort one proc at a time until deadlock cycle gone
	- Ordering of abort:
		1. Priority of process
		1. Process compute time, time left
		1. Resources used
		1. Resources ...
		1. ...
	- Possible starvation doing this

---

- Midterm hints
- Know multi-level queue
- Affinity (hard/soft)
- No code
- Know problems with real-time scheduling (bounding)
- Know monitoring for final
