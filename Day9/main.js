function moveTrain(board, mov) {
    const headRow = board.findIndex(row => row.includes('@'));
    const headCol = board[headRow].indexOf('@');

    const moves = { 'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0] };
    const [dRow, dCol] = moves[mov];
    const newRow = headRow + dRow;
    const newCol = headCol + dCol;

    const newPos = board[newRow]?.[newCol];
    if (!newPos || newPos === 'o') return 'crash';
    if (newPos === '*') return 'eat';

    board[newRow] = board[newRow].slice(0, newCol) + '@' + board[newRow].slice(newCol + 1);
    board[headRow] = board[headRow].slice(0, headCol) + 'o' + board[headRow].slice(headCol + 1);

    return 'none';
}