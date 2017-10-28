# Shared Memory

## Allocate

- To create/allocate a shared memory segment:
```c
#include <sys/ipc.h>
#include <sys/shm.h>

int shmget(key_t key, size_t size, int shmflg);
```
- `key`: identity key
- `size`: memory size
- `IPC_CREAT` is used for `shmflg` when the section is to be allocated
	- If not specified, function *gets* segment based on key
	- Commonly used with permission flags that restrict the memory access
		- `IPC_CREAT | 0666` for server, perhaps, then just `0666` for client
		  - Use when accessing the created segment (server) in subsequent processes (clients)
- If `shmget` returns negative number, request to allocated failed

## Attach

- To attach the already created segment:
```c
#include <sys/types.h>
#include <sys/shm.h>

void *shmat(int shmid, const void *shmaddr, int shmflg);
```
- `shmid`: Id from `shmget`
- `shmaddr`: pointer
	- If NULL, use first address available
	- If not NULL, use for attach address (must be page-aligned)
- `shmflg`: bit-mask for read/write/exec permissions
	- Can use 0
	- `SHM_EXEC`, `SHM_RDONLY`, `SHM_REMAP` (replace existing mapping starting at `shmaddr`
- Returns void pointer, negative number if unsuccessful
- Once this is done, process can access shared memory

## Detach

- To detach shared memory:
```c
#include <sys/types.h>
#include <sys/shm.h>

int shmdt(const void *shmaddr);
 ```
 - `shmaddr`: pointer returned from `shmat`
	 - Detach location
 - Even though detached, can still use again
	 - Must remove to get back memory

## Remove

- To full remove shared memory segment from address space:
```c
#include <sys/ipc.h>
#include <sys/shm.h>

int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```
- `shmid`: Id from `shmget`
- `cmd`: various commands (`IPC_RMID` when deallocating segment)
- `buf`: pointer to a `shmid_ds` structure
	- Contains info about segment (times, PID, owners, permissions)
	- Ignored when `IPC_RMID` used
		- Can set to `NULL` too
	- Used with other values in `cmd`

## Notes

- These code samples were taken from the Linux man pages, not POSIX
- Use `ipcs -m` to view existing shared memory segments
- Use `ipcrm -M shm_key` or `ipcrm -m shm-id` to remove segments
- Great resource [here](http://www.csl.mtu.edu/cs3331.ck/common/03-Process.pdf)
	- Go towards bottom to see shared memory section
