class Assembler:
    def __init__(self):
        pass

    def assemble(self, program: list[str]):
        """Translate the program to CPU accepted format"""
        machine_code: list[tuple] = []

        for instruction in program:

            parts = instruction.split(" ")
            if len(parts) == 2:
                op_code, mem_addr = instruction.split(" ")
            else:
                op_code, mem_addr = instruction.strip().upper(), None

            op_code = op_code.strip().upper()
            mem_addr = int(mem_addr.strip()) if mem_addr != None else mem_addr

            machine_code.append((op_code, mem_addr))
        return machine_code