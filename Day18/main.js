function findInAgenda(agenda, phone) {
  const lines = agenda.split('\n');
  let result = null;

  for (let line of lines) {
    line = line.trim();

    const nameMatch = line.match(/<([^>]+)>/);
    const phoneMatch = line.match(/\+[\d-]+/);

    if (nameMatch && phoneMatch) {
      const name = nameMatch[1];
      const phoneNumber = phoneMatch[0];
      const address = line.replace(nameMatch[0], '').replace(phoneNumber, '').trim();
      if (phoneNumber.includes(phone)) {
        if (result) {
          return null;
        }
        result = { name, address };
      }
    }
  }

  return result;
}