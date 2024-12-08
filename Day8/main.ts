function drawRace(indices: number[], length: number): string {
  const result: string[] = new Array(indices.length);

  for (let i = 0; i < indices.length; i++) {
    const index = indices[i];
    const shift: string = ' '.repeat(indices.length - i - 1);
    const lane: string = ` /${i + 1}`;
    const realIndex: number = ((index % length) + length) % length;
    const reindeerExistence: string = index === 0 ? '' : 'r';

    const raceLine: string = `${'~'.repeat(realIndex)}${reindeerExistence}`.padEnd(length, '~');
    result[i] = shift + raceLine + lane;
  }

  return result.join('\n');
}
