import os.path
import csv
import json

print("Welcome to the JSON-CSV Converter.")
print("This script will convert a JSON file to CSV or a CSV file to JSON")

# SELECT AND OPEN A CSV OR JSON FILE
try:
    print("Which file do you want to convert?")
    filename = input("Filename: ")
    extension = filename.split(".")[1]
    f = open(filename)

    if extension.lower() == "csv":
        # load csv file
        data = list(csv.reader(f))
        print("CSV file loaded")
    elif extension.lower() == "json":
        # load json file
        data = json.load(f)
        print("JSON file loaded")
except:
    # error loading file
    print("Error loading file ... exiting")
    exit()
else:
    # CONVERT CSV TO JSON
    if extension.lower() == "csv":
        keys = data[0]
        converted = []

        for i in range(1, len(data)):
            obj = {}
            for j in range(0,len(data[i])):
                obj[keys[j]] = data[i][j]
            converted.append(obj)
        
        converted_file_basename = os.path.basename(filename).split(".")[0]
        converted_file_extension = ".json"
        if(os.path.isfile(converted_file_basename + converted_file_extension)):
            counter = 1
            while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension):
                counter += 1
            converted_file_basename = converted_file_basename + " (" + str(counter) + ")"

        with open(converted_file_basename + converted_file_extension, 'w') as outfile:
            json.dump(converted, outfile)        

