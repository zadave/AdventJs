def organize_shoes(shoes):
    shoe_map = {}

    for shoe in shoes:
        size = shoe['size']
        shoe_type = shoe['type']
        if size not in shoe_map:
            shoe_map[size] = {'I': 0, 'R': 0}
        shoe_map[size][shoe_type] += 1

    result = []

    for size, counts in shoe_map.items():
        pairs = min(counts['I'], counts['R'])
        result.extend([size] * pairs)

    return sorted(result)
