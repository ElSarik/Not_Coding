def main():

    GRK = request_input()
    change, detailed_change = BankCoins(GRK)

    print(f'change({GRK}) => {change} : {detailed_change[0]} of 500 GRK | ', 
          f'{detailed_change[1]} of 100 GRK | {detailed_change[2]} of 25 GRK |',
          f'{detailed_change[3]} of 10 GRK | {detailed_change[4]} of 5 GRK |',
          f'{detailed_change[5]} of 1 GRK')

    return


# change calculation
def BankCoins(GRK):
    
    # contains the total amount of change for each currency value
    detailed_change = [0, 0, 0, 0, 0, 0]

    currency_values = [500, 100, 25, 10, 5, 1]

    total_change = 0
    change = 0
    
    for index, currency in enumerate(currency_values):
        if GRK >= currency:
            change = int(GRK / currency)
            GRK -= change * currency

            total_change += change
            detailed_change[index] = change
            change = 0

    return total_change, detailed_change


# Requesting user input
def request_input():

    while True:
        try:
            GRK = int(input('Please insert your requested amount: '))
            break

        except:
            print('WARNING: Your input must be an integer number!\n')

    return GRK


if __name__ == '__main__':
    main()