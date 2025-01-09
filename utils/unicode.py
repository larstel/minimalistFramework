from unidecode import unidecode

def use_unidecode(data):
    if isinstance(data, dict):
        return {k: use_unidecode(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [use_unidecode(item) for item in data]
    elif isinstance(data, str):
        return unidecode(data)
    else:
        return data