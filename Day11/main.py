import re


def decode_filename(filename):
    return re.sub(r'(\.\w+$|\d+_)', '', filename)
