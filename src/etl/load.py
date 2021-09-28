# CREATE and INSERT into db table.

import psycopg2
from psycopg2.extras import execute_values
from src import config


def from_json(data_gen):
    """Get the json values. Return [[row]]"""

    all_rows = []
    # for current_dict in data_gen:
    for current_dict in data_gen:
        # current_dict = next(data_gen)
        current_row = []
        for value in current_dict.values():
            # Parse values list into str
            if isinstance(value, list):
                # To insert text not list
                value = ','.join(map(str, value))

            current_row.append(value)

        all_rows.append(current_row)

    return all_rows


# Insert json into postgresql.
def connect_and_load(section, mod_data):
    db_config_params = config.db_config(section)
    try:
        # Process info
        print(f'Connecting to database....')

        # Context manager does the commit and close for us.
        with psycopg2.connect(**db_config_params) as connection:
            with connection.cursor() as cursor:
                # Creat new table if does not exists.
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS lager("
                    "id SERIAL PRIMARY KEY, "
                    "abv REAL, "
                    "name varchar (255), "
                    "first_brewed DATE ,"
                    "food_pairing TEXT, "
                    "tagline TEXT);")

                # Process info
                print('Table was created successfully.')

                # Insert into the table.
                sql_expression = 'INSERT INTO lager (abv, name, first_brewed, food_pairing, tagline) VALUES %s'
                # Nested list to list due to execute_values()
                rows = from_json(mod_data)
                # execute_values preferred due to better performance
                execute_values(cursor, sql_expression, rows)

                # Process info
                print(f"Table 'lager' was created and populated successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
