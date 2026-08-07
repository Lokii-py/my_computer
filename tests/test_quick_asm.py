"""This test need to be updated because program is hardcoded for now.
Once the codebase is is changed, this test should be updated too."""

from CPU.cpu import CPU
from assembler.assembler import Assembler
from loader.loader import Loader


def test_assembler_and_loader():
    cpu = CPU()
    assembler = Assembler()
    loader = Loader()

    program = [
        "LOAD counter",
        "ADD 41",
        "HALT",
    ]

    out = assembler.assemble(program)
    assert out == [("LOAD", 40), ("ADD", 41), ("HALT", None)]

    loader.load(cpu, out, start_addr=10)
    assert cpu.memory[10] == ("LOAD", 40)

    cpu.run()
    assert cpu.ir == ("HALT", None)
