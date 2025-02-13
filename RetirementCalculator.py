import csv

#read the file in
def readCSV(file_path):
    rates = []
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:  # Skip the header
            year, stock, bond = line.strip().split() #splitting strings to take out input
            rates.append((int(year), float(stock.strip('%')) / 100, float(bond.strip('%')) / 100))
    return (rates)

def main():
    rates = readCSV('BondsAndStocksAnnualReturn.csv')

    #ask initial questions
    age = int(input("How old are you? "))
    retirement_age = int(input("At what age do you want to retire? "))

    # take inputs
    mattress = float(input("Please enter the starting balance for money under your mattress: "))
    bank_savings = float(input("Please enter the starting balance for money in bank savings: "))
    bonds = float(input("Please enter the starting balance for money in bonds: "))
    stocks = float(input("Please enter the starting balance for money in stocks: "))

    