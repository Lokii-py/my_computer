from pathlib import Path

from CPU.cpu import CPU
from assembler.assembler import Assembler
from loader.loader import Loader


def test_copy_function():
    current_folder = Path(__file__).parent

    asm_file = current_folder / "copy.asm"
    with open(asm_file, "r") as f:
        program = f.readlines()

    cpu = CPU()
    assembler = Assembler()
    loader = Loader()

    machine_code, data_segment = assembler.assemble(program)
    loader.load(cpu, machine_code, data_segment)

    cpu.run()
    assert cpu.register_a == 8
