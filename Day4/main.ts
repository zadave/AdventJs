function createXmasTree(height: number, ornament: string): string {
  const width = height * 2 - 1;
  const baseLine = '_'.repeat((width - 1) / 2) + '#' + '_'.repeat((width - 1) / 2);
  const tree = Array.from({ length: height }, (_, i) => {
    const ornamentCount = i * 2 + 1;
    const padding = (width - ornamentCount) / 2;
    return '_'.repeat(padding) + ornament.repeat(ornamentCount) + '_'.repeat(padding);
  });
  return [...tree, baseLine, baseLine].join('\n');
}
