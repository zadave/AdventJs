function decodeFilename(filename) {
  return filename.replace(/(\.\w+$|\d+_)/gi, '')
}