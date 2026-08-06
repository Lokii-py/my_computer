class Loader:
    def __init__(self):
        pass

    def load(self, cpu, translator_out: list[tuple], start_addr: int = 0):
        """Load the instruction converted from assembly to cpu parsable instruction"""
        for instruction in translator_out:
            cpu.memory[start_addr] = instruction
            start_addr += 1
