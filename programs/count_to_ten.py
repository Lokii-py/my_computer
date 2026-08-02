from CPU.cpu import CPU

cpu = CPU()

cpu.memory[0] = ("LOAD", 40)
cpu.memory[1] = ("ADD", 41)
cpu.memory[2] = ("COMPARE", 42)
cpu.memory[3] = ("JUMP_IF_ZERO", 5)
cpu.memory[4] = ("JUMP", 1)
cpu.memory[5] = ("HALT", None)

cpu.memory[40] = 0
cpu.memory[41] = 1
cpu.memory[42] = 10

cpu.run()
