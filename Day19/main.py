def distribute_weight(weight: int) -> str:
    box_representations = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"],
    }

    # Lista de pesos ordenada de mayor a menor
    weights = sorted(box_representations.keys(), reverse=True)
    boxes = []

    # Selección de las cajas mínimas
    for box_weight in weights:
        while weight >= box_weight:
            weight -= box_weight
            boxes.append(box_representations[box_weight])

    if weight > 0:
        raise ValueError("No se puede distribuir el peso exacto con las cajas disponibles.")

    # Construcción del apilado reutilizando bordes
    max_width = 0
    stack = []

    for box in reversed(boxes):
        if stack:
            # Reutilizar el borde inferior de la última caja apilada
            box[-1] = box[-1].ljust(max_width, "_")
        max_width = len(box[0].strip())
        stack.extend(box)

    return "\n".join(stack)


# Ejemplo para el peso 3
print(distribute_weight(3))
