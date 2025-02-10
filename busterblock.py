def remove_indices(data):
    """
    Recursively removes numeric indices from nested dictionaries and lists.
    """
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                value = remove_indices(value)
            # If the key is numeric (index), remove it
            if isinstance(key, str) and key.isdigit():
                continue
            new_dict[key] = value
        return new_dict
    elif isinstance(data, list):
        return [remove_indices(item) for item in data]
    else:
        return data
