import csv

#read the file in
def readCSV(file_path):
    rates = []
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:  # Skip the header
            year, stock, bond = line.strip().split() #splitting strings to take out input
            rates.append((int(year), float(stock.strip('%')) / 100, float(bond.strip('%')) / 100))
    return (rates)

rates = readCSV()
print (rates)