from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    head_row = next(i for i, row in enumerate(board) if '@' in row)
    head_col = board[head_row].index('@')

    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    d_row, d_col = moves[mov]

    new_row, new_col = head_row + d_row, head_col + d_col

    if not (0 <= new_row < len(board)) or not (0 <= new_col < len(board[new_row])):
        return 'crash'

    if board[new_row][new_col] in ('o', ' '):
        return 'crash'
    if board[new_row][new_col] == '*':
        return 'eat'

    board[new_row] = board[new_row][:new_col] + '@' + board[new_row][new_col + 1:]
    board[head_row] = board[head_row][:head_col] + 'o' + board[head_row][head_col + 1:]

    return 'none'
