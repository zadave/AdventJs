type Shoe = {
  type: 'I' | 'R';
  size: number;
};

function organizeShoes(shoes: Shoe[]): number[] {
  const shoeMap = new Map<number, { I: number; R: number }>();

  // Contar el número de botas izquierda y derecha por tamaño
  for (const { type, size } of shoes) {
    if (!shoeMap.has(size)) {
      shoeMap.set(size, { I: 0, R: 0 });
    }
    shoeMap.get(size)![type]++;
  }

  const result: number[] = [];

  // Encontrar los pares y añadir el tamaño tantas veces como pares haya
  for (const [size, counts] of shoeMap) {
    const pairs = Math.min(counts.I, counts.R);
    for (let i = 0; i < pairs; i++) {
      result.push(size);
    }
  }

  return result.sort((a, b) => a - b); // Ordenar los tamaños de menor a mayor
}