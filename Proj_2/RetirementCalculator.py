import csv
import os

#read the file in
def readCSV(file_path):
    #rates = []
    #with open(file_path, 'r') as file:
        #for line in file.readlines()[1:]:  # Skip the header
            #year, stock, bond = line.strip().split() #splitting strings to take out input
            #rates.append((int(year), float(stock.strip('%')) / 100, float(bond.strip('%')) / 100))
    #return (rates)
    rates = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)  # Use csv.reader to handle comma-separated values
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            if len(row) != 3:  # Ensure the row has exactly 3 values
                print(f"Skipping malformed line: {','.join(row)}")
                continue
            year, stock, bond = row
            rates.append((int(year), float(stock.strip('%')) / 100, float(bond.strip('%')) / 100))
    return rates


def main():
    rates = readCSV('/Users/gayathrichava/Documents/GitHub/CIS298/Proj_2/BondsAndStocksAnnualReturn.csv')
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 0:
                print("Age cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            retirement_age = int(input("At what age do you want to retire? "))
            if retirement_age <= age:
                print("Retirement age must be greater than your current age. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    mattress = float(input("Please enter the starting balance for money under your mattress: "))
    bank_savings = float(input("Please enter the starting balance for money in bank savings: "))
    bonds = float(input("Please enter the starting balance for money in bonds: "))
    stocks = float(input("Please enter the starting balance for money in stocks: "))

    yearly_balances = []

    for year in range(age, retirement_age):
        print(f"Year {year}: Current balances:")
        print(f"  Mattress: ${mattress:.2f}")
        print(f"  Bank Savings: ${bank_savings:.2f}")
        print(f"  Bonds: ${bonds:.2f}")
        print(f"  Stocks: ${stocks:.2f}")

        while True:
            add_choice = input("Do you want to add money to any account? (yes/no): ").strip().lower()
            if add_choice in ['no', 'n']:  
                break 

            if add_choice not in ['yes', 'y']: 
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

            account = input("Which account? (mattress/bank/bonds/stocks): ").strip().lower()
            if account not in ['mattress', 'bank', 'bonds', 'stocks']:
                print("Invalid account. Try again.")
                continue

            try:
                amount = float(input("How much do you want to add? "))
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if account == 'mattress':
                mattress += amount
            elif account == 'bank':
                bank_savings += amount
            elif account == 'bonds':
                bonds += amount
            elif account == 'stocks':
                stocks += amount

        bank_savings *= 1.02  # fixed 2% return for bank savings
        current_year = 1928 + (year - age)
        for rate in rates:
            if rate[0] == current_year:
                _, stock_rate, bond_rate = rate
                bonds *= (1 + bond_rate)
                stocks *= (1 + stock_rate)
                break

        total_balance = mattress + bank_savings + bonds + stocks
        yearly_balances.append([year, mattress, bank_savings, bonds, stocks, total_balance])


    total_savings = sum([mattress, bank_savings, bonds, stocks])
    inflation_years = retirement_age - age
    adjusted_savings = total_savings / (1.02 ** inflation_years)

    print("\nRetirement Summary:")
    print(f"  Total Mattress Money: ${mattress:.2f}")
    print(f"  Total Bank Savings: ${bank_savings:.2f}")
    print(f"  Total Bonds: ${bonds:.2f}")
    print(f"  Total Stocks: ${stocks:.2f}")
    print(f"  Total Retirement Savings: ${total_savings:.2f}")
    print(f"  Inflation-Adjusted Savings: ${adjusted_savings:.2f}")

    script_dir = os.path.dirname(os.path.abspath(__file__))  
    file_path = os.path.join(script_dir, 'yearly_balances.csv')

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Mattress', 'Bank Savings', 'Bonds', 'Stocks', 'Total'])
        writer.writerows(yearly_balances)

        print("\nChecking yearly_balances before writing to CSV:")
        for row in yearly_balances:
            print(row)

    print(f"Yearly balances successfully saved to '{file_path}'.")

if __name__ == "__main__":
    main() 