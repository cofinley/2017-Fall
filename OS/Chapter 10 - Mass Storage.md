# OS - Chapter 10 Mass Storage Structure


<!-- vim-markdown-toc GFM -->
* [Background](#background)
	* [Hard Disks](#hard-disks)
	* [Solid State Disks](#solid-state-disks)
	* [Magnetic Tape](#magnetic-tape)
* [Disk Structure](#disk-structure)
* [Attachment](#attachment)
* [Disk Scheduling](#disk-scheduling)
	* [Performance](#performance)
* [Disk Management](#disk-management)
* [RAID](#raid)
	* [Extensions](#extensions)

<!-- vim-markdown-toc -->

## Background

- Spinning disk has platters (i.e. 3.5 inch) covered with magnetic material
	- Each platter has concentric **tracks** of info and each track has adjacent **sectors**
- There is a read/write head for every platter
- Disk speed: 
	- Transfer rate
		- Flow speed b/w disk and PC
	- Positioning time
		- Seek time (movement of disk arm to cylinder)
		- Rotational latency: time needed to rotate sector to disk head
- Disk drive attached with wires aka **I/O bus**
	- Examples: ATA, SATA, eSATA, USB
	- Host controller in computer uses bus to talk to disk controller in drive


### Hard Disks

- Transfer rate
	- Theoretica: 6 Gb/sec
	- Effective: 1 Gb/sec
- Average access time = average seek time + average latency
- Average I/O time = average access time + (amount to transfer / transfer rate) + controller overhead


### Solid State Disks

- Nonvolatile
- No moving parts, faster
- Buses can be slow, SSD can connect directly to PCI lane

### Magnetic Tape

- Holds mostly large and permanent data
- Slow access time (1000x slower than disk)

## Disk Structure

- Drives addressed as 1D arrays of logical blocks (smallest unit of transfer)
	- Blocks mapped to disk sectors
		- Sector 0 -> first sector on first track of outermost cylinder
		- Proceed by sector -> track -> cylinders

## Attachment

1. Host-attached (I/O)
2. Network-attached (NAS, remote host)
	- Protocols: NFS, CIFS
	- Implemented with remote procedure calls (RPCs) over TCP, UDP, or IP network

## Disk Scheduling

- Minimize seek time (arm movements to cylinder containing sector)
- OS maintains queue of I/O requests per disk
- Algorithms
	- FCFS
	- Shortest Seek Time First (SSTF)
		- Similar to SJF, may cause starvation
	- SCAN
		- Move from one end of disk to other, servicing requests as it goes over affected sectors
		- AKA elevator algo
	- C-SCAN
		- More uniform wait time than SCAN
		- When head reaches other end, it returns to beginning, and does not go backwards
			- More of a circular list
	- LOOK
		- Arm only goes as far as requests go, then goes backwards, again only as far as needed
	- C-LOOK
		- Arm only goes as far as requests go, then back to the beginning

### Performance

- SCAN, C-SCAN good for heavy disk load as there is less starvation
- Rotational latency hard for OS to calculate
- SSTF or LOOK reasonable as a default

## Disk Management

- Physical Formatting: dividing disk into sectors that disk controller can read/write
- OS needs own data structures on disk to be able to hold its files
	- Partition disk into groups of cylinders
		- Each treated as logical disk
	- Logical formatting AKA making a file system
	- Increase efficiency by grouping blocks into clusters
		- Disk I/O done in blocks
		- File I/O done in clusters

## RAID

- Redundant Array of Inexpensive Disks
- Increases mean time to failure
- **Striping**: uses group of disks as one storage unit
- Six levels
	- 0: Non-redundant striping
	- 1: Mirrored disks
	- 2: Memory-style error correcting codes
	- 3: Bit-interleaved parity
	- 4: Block interleaved parity
	- 5: Block interleaved distributed parity
	- 6: P-Q redundancy
- Mirroring (RAID 1) keeps duplicates of each disk
- Striped mirrors (RAID 1+0) or mirrored stripes (RAID 0+1) gives high performance and reliability
- Block interleaved parity (RAID 4, 5, 6) has much less redundancy

### Extensions

- RAID doesn't prevent or detech corruption, just disk failures
- ZFS adds checksums to all data
	- No volumes/partitions, **pools** instead
		- Pool shared like memory, used and released like `malloc()` and `free()`
