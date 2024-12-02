def create_frame(names):
    max_length = max(map(len, names))
    border = '*' * (max_length + 4)
    frame = [border] + [f"* {name:<{max_length}} *" for name in names] + [border]
    return "\n".join(frame)