from CPU.cpu import CPU


def test_counter_program():
    cpu = CPU()

    assert cpu.pc == 0
    cpu.memory[0] = ("LOAD", 40)
    cpu.memory[1] = ("ADD", 41)
    cpu.memory[2] = ("COMPARE", 42)
    cpu.memory[3] = ("JUMP_IF_ZERO", 5)
    cpu.memory[4] = ("JUMP", 1)
    cpu.memory[5] = ("HALT", None)

    cpu.memory[40] = 0
    cpu.memory[41] = 1
    cpu.memory[42] = 10

    assert cpu.memory[40] == 0

    cpu.run()

    assert cpu.ir == ("HALT", None)
    assert cpu.register_a == 10
