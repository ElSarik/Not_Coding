import random

def main():
    # Loop to keep requesting a number from the user in case of a wrong input
    while True:
        # Displaying all the available options to the user
        print("Which program would you like to use:\n"
              "1. isEven() - Checking if a given number is even or odd\n"
              "2. isPrime() - Checking if a given number is prime or not\n"
              "3. isPrime_2_100() - Displaying all prime numbers between 2 and 100\n"
              "4. fahrenheit_Celsius() - Converting a temperature from Celsius to Fahrenheit, and the opposite\n"
              "5. lottery() - Try to guess 10 randomly generated numbers in a lottery\n"
              "6. Exit - Terminates this program")

        try:
            # Requesting an integer number between 1 and 6 from the user
            selection = int(input("\nPlease enter a number between 1 and 6, based on your selection: "))

            # Checking if number is between 1 and 6
            if (selection >= 1) and (selection <= 6):
                if selection == 1:
                    isEven()

                if selection == 2:
                    isPrime()

                if selection == 3:
                    isPrime_2_100()

                if selection == 4:
                    fahrenheit_Celsius()

                if selection == 5:
                    lottery()

                if selection == 6:
                    return 0

            else:
                print("Please enter a number between 1 and 6!\n")
        except:
            print("Your input was invalid!\n")


def isEven():
    # Loop to keep requesting a number from the user in case of a wrong input
    while True:
        try:
            # Asking user to input an integer: Check passes -> Escaping the loop
            number = int(input("Please enter an integer number: "))
            break
        # Notifying the user about an invalid input -> Repeating the check
        except:
            print("Your input was invalid! \n")

    # Checking if the number is even
    if (number % 2) == 0:
        print(number, "is Even!\n")
    else:
        print(number, "is Odd!\n")

    # Returning back to main()
    return


def isPrime():
    # Loop to keep requesting a number from the user in case of a wrong input
    while True:
        try:
            # Asking user to input an integer: Check passes -> Escaping the loop
            number = int(input("Please enter an integer number: "))
            break
        # Notifying the user about an invalid input -> Repeating the check
        except:
            print("Your input was invalid! \n")

    # Checking if the number is bigger than 1: Check fails -> Number cannot be prime
    if number > 1:
        # Checking for factors between 2 and the number
        for i in range(2, number):
            # if factor exists -> Number is not prime
            if(number % i) == 0:
                print(number, "is not prime!\n")
                break

        # Check has been completed, no factors found -> Number is prime
        else:
            print(number, "is prime!\n")

    # Numbers less than 1 are not prime
    else:
        print(number, "is not a prime number!\n")

    # Returning back to main()
    return


def isPrime_2_100():
    # Taking every number between 2 and 100
        # Checking for factor numbers between 2 and the current number
    for number in range(2, 101):
        for i in range(2, number):
            # if factor exists -> Number is not prime
            if(number % i) == 0:
                # Loop breaks -> Checking the next number in range 2-100
                break

        # Check has been completed, no factors found -> Number is prime
        else:
            print(number)

    print("\n")
    # Returning back to main()
    return


def fahrenheit_Celsius():
    # Loop to keep requesting a number from the user in case of a wrong input
    while True:
        print("Would you like to convert:\n"
              "1. Celsius to Fahrenheit\n"
              "2. Fahrenheit to Celsius")
        try:
            selection = int(input("Please enter the numbers 1 or 2, based on your selection: "))
            # Checking if input is either 1 or 2: Check fails -> Input is requested again
            if (selection == 1) or (selection == 2):

                # Loop to keep requesting a number from the user in case of a wrong input
                while True:
                    try:
                        temperature = float(input("\nPlease enter a temperature: "))

                        # selection 1 -> Converting Celsius to Fahrenheit
                        if selection == 1:
                            conv_temperature = (temperature * 1.8) + 32
                            print(temperature, "degrees Celsius is", conv_temperature, "degrees Fahrenheit!\n")
                            # Breaking the temperature input loop -> returning to selection loop
                            break

                        # selection 2 -> Converting Fahrenheit to Celsius
                        else:
                            conv_temperature = (temperature-32) / 1.8
                            print(temperature, "degrees Fahrenheit is", conv_temperature, "degrees Celsius!\n")
                            # Breaking the temperature input loop -> returning to selection loop
                            break

                    # Error message for invalid temperature
                    except:
                        print("Your input was invalid!")

                # Conversion has been completed -> breaking the selection loop
                break

            # Error message for wrong selection input number
            else:
                print("Your input must be either 1 or 2! \n")

        # Error message for invalid selection input
        except:
            print("Your input was invalid! \n")

    # Returning back to main()
    return


def lottery():
    # Creating an empty list for the generated random numbers
    lottery_draw = []

    # Creating an empty list for the numbers the player has chosen
    player_numbers = []

    # Counter which gets incremented by 1 with every correct guess: lottery_draw[i] == player_numbers[i]
    correct_guesses = 0

    # Loop to generate 10 numbers
    for i in range(0, 10):
        # Generating a random integer between 0 and 9
        random_number = random.randint(0, 9)
        # Appending the generated number into the lottery_draw list
        lottery_draw.append(random_number)

    print("\nWelcome to our lottery!\n"
          "We have drawn 10 numbers from 0 to 9.\n"
          "Can you guess them all and win the grand price?")

    # Main loop for requesting the 10 numbers from the user
    for i in range(len(lottery_draw), 0, -1):
        print("\n", i, "left!")

        # Loop to keep requesting a number from the user in case of a wrong input
        while True:
            try:
                # Asking user to input an integer: Check passes -> Continuing execution
                number = int(input("Please enter an integer number between 0 and 9: "))

                # Checking if input number is between 0 and 9
                if(number >= 0) and (number <= 9):
                    # Appending the user's number to player_numbers
                    player_numbers.append(number)
                    # Breaking out of the loop
                    break

                # Check fails -> Displaying error message to the user -> Requesting a new input
                else:
                    print("Your number must be between 0 and 9!\n")

            # Something other than an integer was given -> Requesting a new input
            except:
                print("Your input must be an integer number!\n")

    # Loop for passing through the 2 lists
    for i in range(0, len(lottery_draw)):
        # Checking if the index i contains the same value in both lists
        if lottery_draw[i] == player_numbers[i]:
            # Check passes -> Incrementing the correct_guesses variable by one
            correct_guesses = correct_guesses + 1

    # Printing results to the user
    print("\nLOTTERY RESULTS:")
    print("player's numbers: ")
    print(player_numbers)
    print("\n lottery numbers:")
    print(lottery_draw)
    print("\n You got", correct_guesses, "correct guesses!\n")

    # Returning back to main()
    return


if __name__ == "__main__":
    main()
