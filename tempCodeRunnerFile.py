import csv

def write_csv():
    with open("reki.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Rollno."])
        writer.writerow(["Rekshit",20 , "0021"])
        writer.writerow(["Ritesh", 19, "0022"])
        writer.writerow(["Ritik", 18, "0023"])
    print("Data written to CSV file successfully")

def read_csv():
    with open("reki.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

write_csv()
print("\nReading data from CSV file:")
read_csv()