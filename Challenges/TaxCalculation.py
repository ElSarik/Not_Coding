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
    
    # calculating cap difference between 0 and first cap
    cap_difference = income_caps[0] - 0

    total_tax = 0

    for index, cap in enumerate(income_caps):
        
        if income > cap_difference:
            if index == 0:
                income_split.append(cap_difference)
                income -= cap_difference
            else:
                cap_difference = cap - income_caps[index - 1]
                income_split.append(cap_difference)
                income -= cap_difference

    # adding the remaining income
    if income > 0:
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
