function isRobotBack(moves: string[]): true | [number, number] {
  let x=0, y=0, seen ={}
  const dir = {L:[-1,0], R:[1,0], U:[0,1], D:[0,-1]}
  const inv = {L:'R', R:'L', U:'D', D: 'U'}

  for (const token of moves.match(/([*!?]?[LRUD])/g) || [])
  {
    let [m, c] = token.length > 1 ? token : ['', token]
    if (m === '!') c = inv[c]
    let [dx,dy] = dir[c]
    if (m === '*') [dx,dy] = [dx*2, dy*2]
    if (m === '?' && seen[c]) continue
    x += dx, y += dy, seen[c] = true
  }
  return x === 0 && y === 0 ? true : [x,y]
}