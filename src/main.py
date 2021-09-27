from etl import extract, transform, load
import pprint


def main():
    raw_api_data = extract.extract_api('api_url')
    fields = ('abv', 'name', 'first_brewed', 'food_pairing', 'tagline')
    transformed_data = transform.modify(raw_data=raw_api_data, fields=fields)
    load.connect_and_load('psql', transformed_data)


if __name__ == "__main__":
    main()
