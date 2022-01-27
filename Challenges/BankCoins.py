def main():
    return


def BankCoins(GRK):
    
    total_change = 0
    change = 0
    

    if GRK >= 500:
        change = int(GRK / 500)
        GRK -= change * 500

        total_change += change
        change = 0


    if GRK >= 100:
        change = int(GRK / 100)
        GRK -= change * 100

        total_change += change
        change = 0


    if GRK >= 25:
        change = int(GRK / 25)
        GRK -= change * 25

        total_change += change
        change = 0


    if GRK >= 10:
        change = int(GRK / 10)
        GRK -= change * 10

        total_change += change
        change = 0


    if GRK >= 5:
        change = int(GRK / 5)
        GRK -= change * 5

        total_change += change
        change = 0


    if GRK >= 1:
        change = int(GRK / 1)
        GRK -= change * 1

        total_change += change
        change = 0


    return total_change


if __name__ == '__main__':
    main()