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
        "counter: DATA 0",
        "LOAD counter",
        "ADD 41",
        "HALT",
    ]

    out, data = assembler.assemble(program)
    assert out == [("LOAD", 40), ("ADD", 41), ("HALT", None)]

    loader.load(cpu, out, data, start_addr=10)
    assert cpu.memory[10] == ("LOAD", 40)

    cpu.run()
    assert cpu.ir == ("HALT", None)
