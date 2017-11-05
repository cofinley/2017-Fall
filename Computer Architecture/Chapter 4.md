# CA - Chapter 4

## Data Path

- To exec instruction, fetch instruction from memory
- Need:
  - Instruction memory
  - PC
  - Adder (to get next address)

![Figure 4.5]()
![Figure 4.6]()

- The second image combines the elements from the first

---

- Processor's registers are stored in __register file__
  - Contains entire register state, can read/write
- Need ALU to operate on values from register file
- Example:
  - R-format instructions (logic & arithmetic)
    - Requires three register operands
      - Read two data words from register file
      - Write one data word
        - Requires two inputs:
          1. Register number
          2. Data to be written
        - Controlled by write control signal

![Register File, figure 4.7]()