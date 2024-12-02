def manufacture(gifts, materials):
    materials_set = set(materials)
    return [gift for gift in gifts if all(char in materials_set for char in gift)]
