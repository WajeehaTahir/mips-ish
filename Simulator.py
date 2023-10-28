class ISA:
    def __init__(self, name):
        self.filename = name
        self.instructions = {}  #to store instructions with line numbers
        self.labels = {}    #label names and their line numbers
        self.data = {}  #to store arrays
        self.registers = {} #registers and their values
        self.pc = 0    #to keep track of current instruction

        with open(self.filename) as f:
            self.instructions = {number: (line.rstrip('\n')).strip() for number, line in enumerate(f)}  #remove spaces from around the instruction and store
            self.labels = {instruction[5:9]: number for number, instruction in enumerate(list(self.instructions.values())) if instruction[0:5] == "10001"} #if the opcode is 10001, extract label name from instruction and store it with its line number 
            f.close()

    def run(self):
        while(self.pc < len(self.instructions)):    #making sure pc is valid
            instruction = self.instructions[self.pc]    #get instruction at program counter
            opcode = instruction[0:5]   #extract opcode
            
            if opcode == "00000":
                self.initialize()
            
            if opcode == "00001":
                self.userInput(instruction[5:8])

            if opcode == "01100":
               self.createArray(instruction[5:9], instruction[9:12])
            
            if opcode == "01001":
                self.immediateValue(instruction[5:8], int(instruction[8:12], 4))

            if opcode == "01011":
                self.store(instruction[5:9], instruction[9:12], instruction[12:15])

            if opcode == "01000":
                self.addImmediate(instruction[5:8], instruction[8:11], instruction[11:15])
            
            if opcode == "00011":
                self.add(instruction[5:8], instruction[8:11], instruction[11:14])

            if opcode == "00100":
                self.sub(instruction[5:8], instruction[8:11], instruction[11:14])
            
            if opcode == "00101":
                self.mul(instruction[5:8], instruction[8:11], instruction[11:14])

            if opcode == "00110":
                self.div(instruction[5:8], instruction[8:11], instruction[11:14])

            if opcode == "01101":
                self.branchGreater(instruction[5:8], instruction[8:11])

            if opcode == "01110":
                self.branchLesser(instruction[5:8], instruction[8:11])

            if opcode == "01111":
                self.branchEqual(instruction[5:8], instruction[8:11])

            if opcode == "10000":
                self.branchNotEqual(instruction[5:8], instruction[8:11])
                
            if opcode == "00111":
                self.jump(instruction[5:9])

            if opcode == "01010":
                self.load(instruction[5:8], instruction[8:12], instruction[12:15])

            if opcode == "00010":
                self.display(instruction[5:8])

            if opcode == "11111":
                break

            self.pc +=1
            
    def initialize(self):
        for i in range(8):
            self.registers[bin(i).replace("0b", "").zfill(3)] = 0   #create registers and set them to zero

    def userInput(self, register):
        self.registers[register] = input()  #store user input in register

    def createArray(self, label, size):
        self.data[label] = [0] * int(self.registers[size])  #create an array in the data segment and initialize it to all zeros

    def immediateValue(self, register, value):
        self.registers[register] = value    #set register to an immediate value

    def store(self, label, offset, source):
        self.data[label][self.registers[offset]] = self.registers[source]   #store value from a register to an array at given offset

    def addImmediate(self, dest, src, value):
        self.registers[dest] = self.registers[src] + int(value, 4)  #add instruction but with immediate value as source2

    def branchGreater(self, r0, r1):
        if int(self.registers[r0]) < int(self.registers[r1]):   #if condition is true, execute next line; else skip next line
            self.pc += 1

    def branchLesser(self, r0, r1):
        if int(self.registers[r0]) > int(self.registers[r1]):
            self.pc += 1

    def branchEqual(self, r0, r1):
        if int(self.registers[r0]) != int(self.registers[r1]):
            self.pc += 1

    def branchNotEqual(self, r0, r1):
        if int(self.registers[r0]) == int(self.registers[r1]):
            self.pc += 1

    def jump(self, target):
        self.pc = self.labels[target]   #get line number of label and set program counter to it

    def load(self, dest, label, offset):
        self.registers[dest] = self.data[label][self.registers[offset]]     #get value from array at given offset and store it to a register

    def display(self, reg):
        print(self.registers[reg])  #print register value

    def add(self, dest, src1, src2):
        self.registers[dest] = int(self.registers[src1]) + int(self.registers[src2])    #get values from two registers and store sum in another register

    def sub(self, dest, src1, src2):
        self.registers[dest] = int(self.registers[src1]) - int(self.registers[src2])

    def mul(self, dest, src1, src2):
        self.registers[dest] = int(self.registers[src1]) * int(self.registers[src2])

    def div(self, dest, src1, src2):
        self.registers[dest] = int(int(self.registers[src1]) / int(self.registers[src2]))

obj = ISA("code.obj")
obj.run()