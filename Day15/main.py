def draw_table(data):
    if not data:
        return ""

    keys = data[0].keys()
    headers = [key.capitalize() for key in keys]

    lengths = {key: len(key) for key in keys}
    for row in data:
        for key in keys:
            lengths[key] = max(lengths[key], len(str(row[key])))

    separator = "+-" + "-+-".join("-" * lengths[key] for key in keys) + "-+"
    header_row = "| " + " | ".join(headers[i].ljust(lengths[key]) for i, key in enumerate(keys)) + "|"

    rows = []
    for row in data:
        row_content = "| " + " | ".join(str(row[key]).ljust(lengths[key]) for key in keys) + "|"
        rows.append(row_content)

    table = [separator, header_row, separator] + rows + [separator]
    return "\n".join(table)