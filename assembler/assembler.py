class Assembler:
    def __init__(self):
        self.symbol = {}
        self.data_segment = {}

    def assemble(self, program: list[str]) -> list[tuple]:
        """Translate the program to CPU accepted format"""
        machine_code: list[tuple] = []

        cleaned_program = self.clean_program(program)

        for instruction in cleaned_program:

            parts = instruction.split(" ")
            if len(parts) == 2:
                op_code = parts[0]
                operand = self.resolve_operand(parts[1])
            else:
                op_code, operand = instruction.strip().upper(), None

            op_code = op_code.strip().upper()
            operand = int(operand) if operand is not None else operand

            machine_code.append((op_code, operand))

        return machine_code, self.data_segment

    def clean_program(self, lines: list[str]) -> list[str]:
        """Clean the assembler format program"""
        if not lines:
            raise ValueError("No program to run. The file is empty")

        inter_program = []
        for line in lines:
            clean_line = line.strip()

            if clean_line == "":
                continue

            if clean_line.startswith("#"):
                continue

            clean_line = clean_line.split("#")[0].strip()
            inter_program.append(clean_line)

        self.create_symbol(inter_program)

        cleaned_program = []
        for line in inter_program:
            if ":" not in line:
                cleaned_program.append(line)

        return cleaned_program

    def create_symbol(self, lines: list[str], mem_addr=40) -> None:
        """Create a symbol for operand look up"""
        count = 0
        for line in lines:
            count += 1
            if ":" in line:
                count -= 1
                x, y = line.split(":")
                x, y = x.strip(), y.strip()
                if y:
                    _, val = y.split()
                    val = int(val)

                    self.symbol[x] = mem_addr
                    self.data_segment[mem_addr] = val

                    mem_addr += 1
                else:
                    self.symbol[x] = count

    def resolve_operand(self, operand):
        """Resolve the Operand into number so CPU can understand it"""
        operand = operand.strip()
        if operand.isdigit():
            return operand
        return self.symbol[operand]
