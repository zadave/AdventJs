function organizeShoes(shoes) {
  const shoeMap = new Map();

  for (const { type, size } of shoes) {
    if (!shoeMap.has(size)) {
      shoeMap.set(size, { I: 0, R: 0 });
    }
    shoeMap.get(size)[type]++;
  }

  const result = [];

  for (const [size, counts] of shoeMap) {
    const pairs = Math.min(counts.I, counts.R);
    for (let i = 0; i < pairs; i++) {
      result.push(size);
    }
  }

  return result.sort((a, b) => a - b);
}