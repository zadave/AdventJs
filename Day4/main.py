def create_xmas_tree(height: int, ornament: str) -> str:
    width = height * 2 - 1
    base_line = ('_' * ((width - 1) // 2)) + '#' + ('_' * ((width - 1) // 2))

    tree = []
    for i in range(height):
        num_ornaments = i * 2 + 1
        spaces = (width - num_ornaments) // 2
        tree.append('_' * spaces + ornament * num_ornaments + '_' * spaces)

    return '\n'.join(tree + [base_line, base_line])

