from configparser import ConfigParser
import csv

def read_properties_file(file_path):
    config = ConfigParser()
    config.read(file_path)
    
    properties_dict = {}
    for section in config.sections():
        for key, value in config.items(section):
            properties_dict[key] = value
    
    return properties_dict


# CSV

def read_csv(file_name, root_path = "./data/csvs/") -> list[list[str]]:
    path = root_path + file_name
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        return list(csv_reader)

    