def draw_race(indices, length):
    result = []
    length_minus_one = length - 1

    for i, index in enumerate(indices):
        shift = ' ' * (len(indices) - i - 1)
        lane = ' ' + f'/{i + 1}'
        real_index = (index % length + length) % length
        reindeer_existence = '' if index == 0 else 'r'

        race_line = ('~' * real_index) + reindeer_existence
        race_line = race_line.ljust(length, '~')
        result.append(shift + race_line + lane)

    return '\n'.join(result)
