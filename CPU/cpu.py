from memory import Memory

class CPU:
    def __init__(self):
        self.register_a: int = 0
        self.pc: int = 0
        self.memory: Memory = Memory(size=256) # memory is an array

    def LOAD(self, mem_addr: int):
        """Load the value in accumulator"""
        self.register_a = self.memory[mem_addr]

    def ADD(self, mem_addr: int):
        """ADD the given Value"""
        self.register_a += self.memory[mem_addr]

    def HALT(self):
        """Stop the program"""
        print("Stopping running")
        self.pc = 0

cpu = CPU()
cpu.LOAD(42)
cpu.ADD(43)
print(cpu.register_a)