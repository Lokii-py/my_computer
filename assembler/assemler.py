class Assembler:
    def __init__(self):
        self.symbol = {
            "counter": 40,
            "one": 41,
        }

    def assemble(self, program: list[str]):
        """Translate the program to CPU accepted format"""
        machine_code: list[tuple] = []

        for instruction in program:

            parts = instruction.split(" ")
            if len(parts) == 2:
                op_code = parts[0]
                operand = self.resolve_operand(parts[1])
            else:
                op_code, operand = instruction.strip().upper(), None

            op_code = op_code.strip().upper()
            operand = int(operand) if operand != None else operand

            machine_code.append((op_code, operand))
        return machine_code

    def resolve_operand(self, operand):
        """Resolve the Operand into number so CPU can understand it"""
        operand = operand.strip().lower()
        if operand.isdigit():
            return operand
        return self.symbol[operand]
