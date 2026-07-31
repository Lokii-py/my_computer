from .memory import Memory

class CPU:
    def __init__(self):
        """Initiating a CPU architecture"""
        self.running: bool = True

        # CPU required quick memory
        self.register_a: int = 0
        self.pc: int = 0
        self.ir: tuple = ()

        self.memory: Memory = Memory(size=256) # memory is an array

    def run(self):
        """Run the CPU in FETCH-DECODE-EXECUTE CYCLE"""
        print("CPU ON:")
        print(f" Program Counter:      {self.pc}")
        print(f" Instruction Register: {self.ir}")
        print(f" Register A:           {self.register_a}")

        while self.running:
            # Fetch the current instruction pointed by pointer
            self.FETCH()

            # Decode the instruction
            op_code, mem_addr = self.DECODE()

            # Execute the instruction
            func = getattr(self, op_code, None)
            if callable(func):  
                func(mem_addr) if op_code != "HALT" else self.HALT()
            else:
                raise ValueError(f"This {op_code} cannot be run. Not Implemented!")

            print("----------------------------------")
            print(f" Program Counter:      {self.pc}")
            print(f" Instruction Register: {self.ir}")
            print(f" Register A:           {self.register_a}")
    
    def FETCH(self):
        """Hold the instruction in instruction register"""
        self.ir = self.memory[self.pc]

    def DECODE(self):
        """Decode the Instruction saved"""
        opcode = self.ir[0]
        mem_addr = self.ir[1] if len(self.ir) == 2 else None
        return opcode, mem_addr

    def LOAD(self, mem_addr: int):
        """Load the value in accumulator"""
        self.register_a = self.memory[mem_addr]
        self.pc += 1

    def ADD(self, mem_addr: int):
        """ADD the given Value"""
        self.register_a += self.memory[mem_addr]
        self.pc += 1

    def HALT(self):
        """Stop the program"""
        print(" PROGRAM HALT!")
        self.running = False
