def min_moves_to_stables(reindeer, stables):
    reindeer.sort()
    stables.sort()

    total_moves = sum(abs(r - s) for r, s in zip(reindeer, stables))
    return total_moves

