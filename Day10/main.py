def compile(instructions):
    registers = {}
    pointer = 0

    while pointer < len(instructions):
        parts = instructions[pointer].split()
        command, *args = parts

        if command == 'MOV':
            registers[args[1]] = int(args[0]) if args[0].isdigit() else registers.get(args[0], 0)
        elif command == 'INC':
            registers[args[0]] = registers.get(args[0], 0) + 1
        elif command == 'DEC':
            registers[args[0]] = registers.get(args[0], 0) - 1
        elif command == 'JMP':
            if registers.get(args[0], 0) == 0:
                pointer = int(args[1])
                continue

        pointer += 1

    return registers.get('A')
