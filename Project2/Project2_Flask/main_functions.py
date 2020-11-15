import json

def read_from_file(file_name):
    with open(filename,"r") as read_file:
        data = json.load(read_file)
        