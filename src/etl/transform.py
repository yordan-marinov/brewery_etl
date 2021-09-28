# Transforms raw data .


def date_format(date_str):
    """Formats date to yyyy-mm-dd. Returns date as string"""

    # The day in row data is not supplied
    day = '01'
    split_date = date_str.split('/')
    # When month is not supplied
    if len(split_date) < 2:
        month, year = '01', split_date[0]
    else:
        month, year = split_date

    return f'{year}-{month}-{day}'


def modify(raw_data, fields):
    """Generator modify raw data. Yield dict"""

    while True:
        try:
            dict_item = next(raw_data)
            current_item = {}
            for field in fields:
                if field == 'first_brewed':
                    new_date = date_format(dict_item[field])
                    current_item[field] = new_date
                else:
                    current_item[field] = dict_item[field]

            yield current_item
        except StopIteration:
            break
