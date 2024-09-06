import csv
import pandas as pd

# Read as list
print("-------Read as list-------")
with open("Courses.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Read as dictionary
print("\n-------Read as dictionary-------")
with open("Courses.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# Read as pandas DataFrame
print("\n-------Read as pandas DataFrame-------")
data = pd.read_csv("Courses.csv")
print(data)

# Read file with \t as delimiter
print("\n-------Read file with \t as delimiter-------")
with open("Courses_space_separated.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=" ")
    for row in csv_reader:
        print(row)


# Write to file
print("\n-------Write to file-------")
people = [
    {"Name": "John", "Age": 30},
    {"Name": "Doe", "Age": 25},
    {"Name": "Smith", "Age": 35}
]
with open("People.csv", mode="w", newline="") as file:
    headers = ["Name", "Age"]
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(people)
print("File written successfully")


# Write to file using list of lists
print("\n-------Write to file using list of lists-------")
people = [
    ["Name", "Age"],
    ["John", 30],
    ["Doe", 25],
    ["Smith", 35]
]
with open("People_v2.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(people)
print("File written successfully")


# Write to file using list of list and delimiter is |
print("\n-------Write to file using list of list and delimiter is |-------")
people = [
    ["Name", "Age"],
    ["John", 30],
    ["Doe", 25],
    ["Smith", 35]
]
with open("People_v3.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file, delimiter="|")
    csv_writer.writerows(people)

# Write to file using list of list and delimiter is | and quotechar is ~
print("\n-------Write to file using list of list and delimiter is | and quotechar is ~-------")
rows = [
    ['Name', 'Branch', 'Year', 'CGPA'],
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

filename = 'students_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,
                        delimiter='|', quotechar='~')
    writer.writerows(rows)

print(f"Data has been written to {filename}")

