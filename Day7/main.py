import re


def fix_packages(packages):
    while '(' in packages:
        packages = re.sub(r'\(([^()]+)\)', lambda match: match.group(1)[::-1], packages)
    return packages
