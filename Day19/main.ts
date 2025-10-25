function distributeWeight(weight: number): string {
  const boxRepresentations = {
    1: [" _ ", "|_|"],
    2: [" ___ ", "|___|"],
    5: [" _____ ", "|     |", "|_____|"],
    10: [" _________ ", "|         |", "|_________|"]
  }

  return Object.keys(boxRepresentations)
    .sort((a, b) => b - a)
    .map(capacity => {
      const qty = Math.trunc(weight / capacity)
      weight -= qty * capacity
      return boxRepresentations[capacity].join('\n').repeat(qty)
    })
    .reverse()
    .join('')
    .replace(/(?<=(\|.+\|))( _+ )(?=\n(\|.+))/gm,
      (remainTop, top) => '_'.repeat(Math.max(0, remainTop.length - top.length - 1)))
}
