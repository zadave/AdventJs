import re

def find_in_agenda(agenda, phone):
    agenda_map = {}

    for line in agenda.split('\n'):
        name_match = re.search(r'<([\w\s]+)>', line)
        phone_match = re.search(r'\+([\d\-]+)', line)

        if not name_match or not phone_match:
            continue

        name = name_match.group(1)
        phone_number = phone_match.group(1)
        address = re.sub(r'<[\w\s]+>', '', line)
        address = re.sub(r'\+[\d\-]+', '', address).strip()

        if phone_number in agenda_map:
            return None

        agenda_map[phone_number] = {'name': name, 'address': address}

    # Find keys containing the phone substring using `find()`
    filtered_keys = [key for key in agenda_map.keys() if key.find(phone) != -1]

    # Return the appropriate result based on the number of matches
    if len(filtered_keys) == 1:
        return agenda_map[filtered_keys[0]]
    return None
