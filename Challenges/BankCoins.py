def main():
    return


# change calculation
def BankCoins(GRK):
    
    # contains the total amount of change for each currency value
    detailed_change = [0, 0, 0, 0, 0, 0]

    total_change = 0
    change = 0
    

    if GRK >= 500:
        change = int(GRK / 500)
        GRK -= change * 500

        total_change += change
        detailed_change[0] = change
        change = 0


    if GRK >= 100:
        change = int(GRK / 100)
        GRK -= change * 100

        total_change += change
        detailed_change[1] = change
        change = 0


    if GRK >= 25:
        change = int(GRK / 25)
        GRK -= change * 25

        total_change += change
        detailed_change[2] = change
        change = 0


    if GRK >= 10:
        change = int(GRK / 10)
        GRK -= change * 10

        total_change += change
        detailed_change[3] = change
        change = 0


    if GRK >= 5:
        change = int(GRK / 5)
        GRK -= change * 5

        total_change += change
        detailed_change[4] = change
        change = 0


    if GRK >= 1:
        change = int(GRK / 1)
        GRK -= change * 1

        total_change += change
        detailed_change[5] = change
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