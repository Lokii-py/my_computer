from CPU.cpu import CPU

cpu = CPU()

cpu.memory[0] = ("LOAD", 42)
cpu.memory[1] = ("ADD", 43)
cpu.memory[2] = ("STORE", 44)
cpu.memory[3] = ("HALT", None)

cpu.memory[42] = 7
cpu.memory[43] = 5

cpu.run()
