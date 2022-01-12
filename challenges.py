def main():
    TotalValueOfCharacters()
    return 0

def TotalValueOfCharacters():

    user_input = 0

    while type(user_input) != str:
        user_input = request_input()

    # Converting the characters to lowercase
    result = upper_to_lowercase(user_input)
    joined_result = ''.join(result)

    if(user_input.casefold() == joined_result.casefold()):
        print(f'{user_input} was converted to {joined_result}')
    else:
        print('There was no conversion necessary.')

    # Calculating the value of the characters
    sum = string_value_calculation(result)

    print(f'The value of the sequence {joined_result} is: {sum}')

    return 0


    # Requesting user input
    def request_input():

        sequence = input('Please write a sequence of alphabetic characters: ')

        if sequence.isalpha():
            return sequence
        else:
            print('Your input must contain only alphabetic characters!\n')


    # Adding characters a - z to a list
    def characters_init():

        characters = []

        for char in range (97, 122+1):
            characters.append(chr(char))

        return characters


    # Converting uppercase characters to lowercase
    def upper_to_lowercase(user_input):

        user_input_list = list(user_input)

        # Converting every uppercase character to lowercase
        for index, char in enumerate(user_input_list):
            if ord(char) < 97:
                user_input_list[index] = chr(ord(char) + 32)

        return user_input_list


    # Calculation of character value
    def string_value_calculation(user_input):

        characters = characters_init()

        sum = 0
        
        # Adding the sum of all the characters based on their index value + 1
        for char in user_input:
            value = characters.index(char)
            sum += value + 1

        return(sum)


if __name__ == "__main__":
    main()