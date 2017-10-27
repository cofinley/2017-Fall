2017/10/26

Virtual Memory

Thrashing
  Not enough pages, too many page faults
  Process too busy swapping pages in and out
  CPU utilized very little
  Total # of pages referenced in working set window needs to be balanced
    Too low: thrashing
    Too high: too much of program covered

Memory-Mapped Files
  Files on disk can be mapped into memory
    Subsequent reads are just reading from memory instead of I/O
    Brought into kernel memory
      Different than user memory
      Draws from free mem pool
      Needs to be contiguous memory for device I/O
      
Buddy System
  One way to manage contiguous memory
  Disadvantage is small data not efficient - leads to internal fragmentation
  
Slabs
  Another way
  Good because no fragmentation
  
Prepaging
  Reduce initial page faults by loading all/some pages a process will need before they're referenced
  Risk of wasting memory and I/O if pages never referenced
  
TLB
  Program structure
    Row and column-major page faults
      Where each __row__ stores one page
        Going by row x column (double for loop) only produces row # of page faults
        Going by column x row produces column*row # of page faults
        Since each row stores one page, going row by row significantly reduces page faults rather than going column by column