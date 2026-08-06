"""Act like Operating Console for now"""

import argparse

from CPU.cpu import CPU
from assembler.assemler import Assembler
from loader.loader import Loader


def main():
    parser = argparse.ArgumentParser(desc="takes assembly program")

    parser.add_argument(
        "asm_path", help="Path to the assmebly program e.g. ./programs/counter.asm"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Whether you want to see the intial state or not",
    )
    parser.add_argument(
        "--trace", action="store_true", help="If you want to see the CPU action"
    )

    args = parser.parse_args()

    with open(args.asm_path, "r") as f:
        program = f.readlines()

    cpu = CPU()
    assembler = Assembler()
    loader = Loader()

    out = assembler.assemble(program)
    print(out)  # debug | should be in trace or debug later

    loader.load(cpu, out)
    cpu.run(debug=args.debug)


if __name__ == "__main__":
    main()
