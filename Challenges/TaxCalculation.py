def main():

    income = request_input()
    tax = TaxCalculation(income)

    print(f'You are expected to pay {tax} in taxes!')

    return


def TaxCalculation(income):
    income_caps = [10000, 30000, 100000]
    tax_rates = [0, 0.10, 0.25, 0.40]

    # spliting the income based on the income_caps
    income_split = []

    total_tax = 0

    for cap in income_caps:
        if income > cap:
            income_split.append(cap)
            income -= cap

    # adding the remaining income
    income_split.append(income)

    # calculating the tax based on each cap
    for index, split in enumerate(income_split):
        tax = split * tax_rates[index]
        total_tax += tax

    
    return total_tax


# Requesting user input
def request_input():

    while True:
        try:
            income = int(input('Please enter your income: '))
            break

        except:
            print('WARNING: Your input must be an integer number!\n')

    return income


if __name__ == '__main__':
    main()