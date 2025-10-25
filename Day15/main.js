function drawTable(data) {
  const keys = Object.keys(data[0])
  const headers = keys.map((key) => key.charAt(0).toUpperCase() + key.slice(1))

  const lengths = {}
  for (let key of keys) {
    lengths[key] = key.length
    for (let row of data) {
      const length = `${row[key]}`.length
      if (length > lengths[key]) {
        lengths[key] = length
      }
    }
  }

  const separator =
    '+-' + keys.map((key) => '-'.repeat(lengths[key])).join('-+-') + '-+'
  const headerRow =
    '| ' +
    keys.map((key, i) => headers[i].padEnd(lengths[key])).join(' | ') +
    ' |'

  const rows = []
  for (let row of data) {
    const rowContent =
      '| ' +
      keys.map((key) => String(row[key]).padEnd(lengths[key])).join(' | ') +
      ' |'
    rows.push(rowContent)
  }

  const table = [separator, headerRow, separator, ...rows, separator]
  return table.join('\n')
}