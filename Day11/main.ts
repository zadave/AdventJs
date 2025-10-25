function decodeFilename(filename: string): string {
      return filename.replace(/(\.\w+$|\d+_)/gi, '')
  }