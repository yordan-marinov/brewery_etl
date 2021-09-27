# Transforms raw data with give params.


def modify(raw_data: list, fields: tuple):
    """New json obj with given fields. Returns list of json."""

    modified_data = []
    for item in raw_data:
        current_item = {}
        for field in fields:
            current_item[field] = item[field]
        modified_data.append(current_item)

    return modified_data
