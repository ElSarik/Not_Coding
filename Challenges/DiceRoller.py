import random
import re

def main():
    matches = RequestInput()

    multiplier_list, dice_number_list = InputCleanup(matches)

    dice_sum_list = DiceRoller(multiplier_list, dice_number_list)

    for index, match in enumerate(matches):
        print(f'{match} results in {dice_sum_list[index]} | '
              f'Between {multiplier_list[index]} and {multiplier_list[index] * dice_number_list[index]}')

    return


# Rolls a random number between 1 and dice_number * multiplier
# Calculates the summation of all rolls
def DiceRoller(multiplier_list, dice_number_list):
    dice_sum_list = []

    for index, multiplier in enumerate(multiplier_list):
        dice_sum = 0

        for roll in range(multiplier):
            dice_sum += random.randint(1, dice_number_list[index])

        dice_sum_list.append(dice_sum)

    return dice_sum_list


# Separating the matches into multiplier and dice_number
def InputCleanup(matches):
    multiplier_list = []
    dice_number_list = []

    for match in matches:
        multiplier, dice_number = match.split('d', 1)

        # Appending multipler and dice_number in lists as integers
        multiplier_list.append(int(multiplier))
        dice_number_list.append(int(dice_number))

    return multiplier_list, dice_number_list


# Requesting user input
def RequestInput():
    regex = '[0-9]{1,}d{1}[0-9]{1,}'
    matches = []

    while not matches:
        user_input = str(input('Please enter a dice or dices in NdM format: '))

        matches = re.findall(regex, user_input) # Finding all regex matches in input

    return matches


if __name__ == "__main__":
    main()