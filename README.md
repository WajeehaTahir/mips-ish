# MIPS-ish ISA (Instruction Set Architecture)

A Python-based ISA inspired by MIPS, designed to simulate a simplified Instruction Set Architecture. This ISA allows for programming in a MIPS-like assembly language, defining various instructions and their functionalities, supporting basic operations, conditional branching, memory handling, and I/O functionalities.

### Features
- **Instruction Set:** Offers a range of fundamental instructions to manage registers, memory, arithmetic, and conditional operations.
- **Register Management:** Eight registers available for operations, each represented by a 3-bit identifier.
- **Memory:** Supports a memory size of 16 bytes with 4-bit addresses, allowing for array creation and manipulation.
- **Input/Output:** Input instruction reads user input, output instruction prints register values to the console.
- **Control Flow:** Conditional branching supported based on comparison operations.

### Usage
The ISA is implemented as a Python class providing methods for executing the program defined in assembly-like language. The supported instructions and their formats are clearly detailed.

### Implementation Details
The core of the ISA resides in the `ISA` class, where the `run` method processes the instructions and performs the associated operations according to the defined opcode. Instructions are represented with their respective opcodes and bit formats, following a structured pattern.

### Supported Instructions
The ISA supports various instructions:

- **Init:** Initialize registers (All register values set to 0).
- **Halt:** Indicates the end of the program.
- **Input & Output:** Read and display values from/to the console.
- **Arithmetic Operations:** Add, Subtract, Multiply, Divide.
- **Memory Operations:** Load, Store, Create Array.
- **Control Flow Instructions:** Jump, Conditional Branching (Greater Than, Less Than, Equal, Not Equal).
- **Immediate Value Operations:** Load an immediate value into a register.

### Instruction Format
Each instruction follows a specific format based on the opcode, register identifiers, memory addresses, and immediate values.

### Benchmark Program
An example benchmark program is provided in the form of a `.asm` file and converted to a `.obj` file, showcasing the usage of the MIPS-ish ISA. The benchmark program demonstrates a sequence of instructions to create an array, perform iterative operations, and finally output the result.

### Getting Started
To start using the MIPS-ish ISA, follow these steps:
1. Write assembly-like code following the supported instructions and their formats.
2. Save the code with a `.asm` extension.
3. Assemble the code using the provided implementation to generate the corresponding `.obj` file.
4. Utilize the `ISA` class to execute the assembled `.obj` file and observe the program's output.

#### Example Assembly Code:
```assembly
init
input r0
array a, r0
im r1, 0
label loop:
    input r2
    store a:r1, r2
    addi r1, r1, 1
    > r1, r0
    jump exit_loop
    jump loop
label exit_loop:
    im r2, 0
    im r3, 0
label sum:
    load r1, a:r2
    add r3, r3, r1
    addi r2, r2, 1
    > r2, r0
    jump exit_sum
    jump sum
label exit_sum:
    output r3
    halt
```
##### Binary Equivalent:
```plaintext
000000000000000
000010000000000
011000000000000
010010010000000
100010001000000
000010100000000
010110000001010
010000010010001
011010010000000
001110010000000
001110001000000
100010010000000
010010100000000
010010110000000
100010011000000
010100010000010
000110110110010
010000100100001
011010100000000
001110100000000
001110011000000
100010100000000
000100110000000
111110000000000
```
### Note
The provided implementation of the MIPS-ish ISA is a simplified version, inspired by MIPS architecture.

*Documented by ChatGPT*
