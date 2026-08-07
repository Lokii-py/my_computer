from CPU.cpu import CPU


def test_my_cpu_intitalization():
    my_cpu = CPU()
    assert my_cpu.pc == 0

    my_cpu.memory[0] = ("LOAD", 42)
    my_cpu.memory[1] = ("ADD", 43)
    my_cpu.memory[2] = ("STORE", 44)
    my_cpu.memory[3] = ("HALT", None)

    my_cpu.memory[42] = 7
    my_cpu.memory[43] = 5

    my_cpu.run()

    assert my_cpu.memory[44] == 12
