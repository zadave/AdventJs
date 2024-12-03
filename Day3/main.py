def organize_inventory(inventory):
    organized = {}
    for item in inventory:
        category, name, quantity = item['category'], item['name'], item['quantity']
        organized[category] = organized.get(category, {})
        organized[category][name] = organized[category].get(name, 0) + quantity
    return organized
