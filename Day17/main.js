function detectBombs(grid) {
  const rows = grid.length;      // Número de filas
  const cols = grid[0].length;   // Número de columnas

  // Creamos una cuadrícula para los resultados
  const result = Array.from({ length: rows }, () => Array(cols).fill(0));

  // Dirección de las 8 posiciones adyacentes (incluidas diagonales)
  const directions = [
    [-1, -1], [-1, 0], [-1, 1], // Arriba: izq, centro, der
    [0, -1],         [0, 1],    // Izquierda y derecha
    [1, -1], [1, 0], [1, 1]     // Abajo: izq, centro, der
  ];

  // Recorrer la cuadrícula
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      // Si la celda actual tiene una bomba, actualizamos las celdas adyacentes
      if (grid[i][j]) {
        for (const [dx, dy] of directions) {
          const newRow = i + dx;
          const newCol = j + dy;

          // Aseguramos que la celda adyacente está dentro de los límites
          if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
            result[newRow][newCol]++;
          }
        }
      }
    }
  }

  return result;
}