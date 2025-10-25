def calculate_price(ornaments):
    prices = {'*': 1, 'o': 5, '^': 10, '#': 50, '@': 100}
    total = 0

    for i in range(len(ornaments)):
        ornament = ornaments[i]
        if ornament not in prices:
            return None

        next_price = prices.get(ornaments[i + 1], 0) if i + 1 < len(ornaments) else 0
        total += prices[ornament] if prices[ornament] >= next_price else -prices[ornament]

    return total
