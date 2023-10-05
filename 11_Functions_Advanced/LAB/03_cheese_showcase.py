def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for name, quantities in sorted_dict:
        result += f"{name}\n"
        sorted_quantities = sorted(quantities, reverse=True)
        result += '\n'.join([str(el) for el in sorted_quantities])
        result += "\n"
    return sorted_dict
