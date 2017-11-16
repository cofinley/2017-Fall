# Group 4 OS Final Project Readme

> Connor Finley, Abhimanyu Dakwale, Raymond Lian
>
>
> Readers-writers Problem, version 2
>
> 2017/11/07

## Usage

### Compiling

- To compile, go to the project directory and run:
	- ```gcc ReaderWriter.c -lpthread -lrt```

- Then, to run, type:
	- ```./a.out```

### Changing Values

- There are several values to change:
	- File name
	- Maximum number of readers
	- Maximum number of writers
	- Strings to write to the file
	- String to initialize the file

#### File name

- To change the file name that the program reads and writes from, navigate to the top of `ReaderWriter.c` and change `FILENAME` to what ever file name you want. Currently, it is `"mytest.dat"`.

#### Maximum Number of Readers and Writers

- These numbers specify the number of dynamic reader and writer threads that will be created
- To change these limits, navigate to the top of `ReaderWriter.c` and change `MAX_WRITERS` and `MAX_READERS` to what ever values you want. Do note that the `MAX_WRITERS` **cannot go above the number of strings provided** in the next section.

#### Strings to Write

- These are the strings picked out for each dynamic writer thread to write
- To change, just alter `writerArray` strings (comma separated). Do not exceed `MAX_WRITERS` number of strings, though.

#### String to initialize file

- Each program run will reset the file so the readout doesn't keep growing in length
- To change, go to function `resetFile()` in `ReaderWriter.c` and change the string `s` from the default "Hi!" to whatever you wish.
