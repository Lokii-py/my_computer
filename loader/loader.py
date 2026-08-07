class Loader:
    def __init__(self):
        pass

    def load(
        self, cpu, translator_out: list[tuple], data_segment: dict, start_addr: int = 0
    ):
        """Load the instruction converted from assembly to cpu parsable instruction"""
        cpu.pc = start_addr

        for instruction in translator_out:
            cpu.memory[start_addr] = instruction
            start_addr += 1
        for idx, val in data_segment.items():
            if data_segment:
                cpu.memory[idx] = val
