function prepareGifts(gifts) {
  const uniqueGifts = new Set(gifts);
  return Array.from(uniqueGifts).sort((a, b) => a - b);
}
