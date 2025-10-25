function compile (instructions: string[]): number {
  const registers = {};
    let pointer = 0;

    while (pointer < instructions.length) {
        const [command, arg1, arg2] = instructions[pointer].split(' ');

        if (command === 'MOV') registers[arg2] = isNaN(arg1) ? (registers[arg1] || 0) : +arg1;
        else if (command === 'INC') registers[arg1] = (registers[arg1] || 0) + 1;
        else if (command === 'DEC') registers[arg1] = (registers[arg1] || 0) - 1;
        else if (command === 'JMP' && !(registers[arg1] || 0)) {
            pointer = +arg2;
            continue;
        }

        pointer++;
    }

    return registers.A;
}