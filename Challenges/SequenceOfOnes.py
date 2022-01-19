def main():

    sequence = request_input()
    result = SequenceOfOnes(sequence)

    print(f'values({sequence}) => {result}')

    return 0


# Calculating the sequence of 1s
def SequenceOfOnes(list):

    sequence_counter = 0
    result = []

    for index, digit in enumerate(list):
        if digit == 1:
            sequence_counter += 1

            # appending counter when at the end of list
            if index == len(list) -1:
                result.append(sequence_counter)

            else:
                # appending counter when next number is a 0
                if list[index + 1] == 0:
                    result.append(sequence_counter)
                    sequence_counter = 0

    return result


# Requesting user input
def request_input():

    sequence = []

    user_input = input('Please write a sequence of 0s and 1s: ')
    input_list = list(user_input)

    # Keeping only '0' and '1' characters
    for element in input_list:
        if element == '0' or element == '1':
            sequence.append(int(element))

    return sequence
    

if __name__ == "__main__":
    main()