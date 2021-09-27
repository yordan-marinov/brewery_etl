# CREATE and INSERT into db table.

import psycopg2
from psycopg2.extras import execute_values
from src import config
from typing import List


def from_json_values(data_list: List[dict]):
    """Get the json values. Return nested list"""

    values = []
    for current_dict in data_list:
        current_row = []
        for value in current_dict.values():
            # Parse values list into str
            if isinstance(value, list):
                value = ','.join(map(str, value))
            current_row.append(value)
        values.append(current_row)

    return values


# Insert json into postgresql.
def connect_and_load(section, mod_data):
    db_config_params = config.db_config(section)
    try:
        print(f'Connecting to database....')
        with psycopg2.connect(**db_config_params) as connection:
            with connection.cursor() as cursor:
                # Creat new table if does not exists.
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS lager("
                    "id SERIAL PRIMARY KEY, "
                    "name varchar (255), "
                    "abv REAL, "
                    "first_brewed VARCHAR (255),"
                    "food_pairing TEXT, "
                    "tagline TEXT);")

                # Insert into the table.
                rows = from_json_values(mod_data)

                sql_expression = 'INSERT INTO lager (abv, name, first_brewed, food_pairing, tagline) VALUES %s'

                # execute_values preferred due to better performance
                execute_values(cursor, sql_expression, rows)

                connection.commit()

                print(f"Table 'lager' was created and populated successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
