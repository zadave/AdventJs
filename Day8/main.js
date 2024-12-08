function drawRace(indices, length) {
  const result = new Array(indices.length);

  for (let i = 0; i < indices.length; i++) {
    const index = indices[i];
    const shift = ' '.repeat(indices.length - i - 1);
    const lane = ` /${i + 1}`;
    const realIndex = ((index % length) + length) % length;
    const reindeerExistence = index === 0 ? '' : 'r';

    const raceLine = `${'~'.repeat(realIndex)}${reindeerExistence}`.padEnd(length, '~');
    result[i] = shift + raceLine + lane;
  }

  return result.join('\n');
}
