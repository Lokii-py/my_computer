from CPU.cpu import CPU
from assembler.assemler import Assembler
from loader.loader import Loader

cpu = CPU()
assembler = Assembler()
loader = Loader()

program = [
    "LOAD counter",
    "ADD 41",
    "HALT",
]

out = assembler.assemble(program)
print(out)

loader.load(cpu, out)
cpu.run()