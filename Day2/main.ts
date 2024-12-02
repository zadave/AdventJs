function createFrame(names: string[]): string {
  const SYMBOL = '*';
  const PADDING = 4;
  const maxLength = names.reduce((max, name) => Math.max(max, name.length), 0) + PADDING;
  const borderLine = SYMBOL.repeat(maxLength);
  const breakLine = '\n';

  const frameContent = names.map(name => {
    const space = ' '.repeat(maxLength - name.length - 3);
    return `* ${name}${space}*${breakLine}`;
  }).join('');

  return borderLine + breakLine + frameContent + borderLine;
}
