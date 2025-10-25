import re

def remove_snow(s):
    regex_snow = re.compile(r"(\w)\1")
    snow = regex_snow.search(s)
    while snow:
        s = regex_snow.sub("", s, count=1)
        snow = regex_snow.search(s)
    return s