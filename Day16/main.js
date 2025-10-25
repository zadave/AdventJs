function removeSnow(s) {
  const regexSnow = /(\w)\1/g;
  let snow = s.match(regexSnow);
   while(snow?.length > 0) {
    s = s.replace(snow[0], "")
    snow = s.match(regexSnow);
  }
  return s;
}