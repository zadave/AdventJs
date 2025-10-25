function calculatePrice(ornaments) {
  const prices = {
    '*': 1, 'o': 5, '^': 10, '#': 50, '@': 100,
  }
  const total = Array.from(ornaments).reduceRight((sum, ornament, i)=>{
    const price = prices[ornament]
    const rightPrice = prices[ornaments[i+1]]
    return [sum + price, sum - price][(+(rightPrice > price))]
  }, 0)
  return [undefined, total][+!!total]
}