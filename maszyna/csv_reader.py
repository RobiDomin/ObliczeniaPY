import csv
import config


def convert_value(value):
    if "," in value:
        try:
            return float(value.replace(",", "."))
        except ValueError:
            return value
    elif value.isdigit():
        return int(value)
    else:
        return value


def read_csv():
    with open(config.CSV_FILE_PATH, 'r', encoding=config.ENCODING) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=config.DELIMITER)
        headers = next(csv_reader)
        data = [[convert_value(cell) for cell in row] for row in csv_reader]
    return headers, data
