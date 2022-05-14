import copy


def main():
    # sample_input = [0,1,0]
    sample_input = [0,1,0,0,1,1,0]

    expected_result = []
    for card in range (0, len(sample_input)):
        expected_result.append("X")


    result = bfs_solution(sample_input, expected_result)
    
    print(result)

    return


def bfs_solution(sample_input, expected_result):

    possible_states = []
    cards_removed = []

    possible_states.append((sample_input, cards_removed))

    for state in possible_states:

        last_state, last_card = possible_states[-1]
        if last_state == expected_result:
            return last_card

        for position, card in enumerate(state[0]):
            current_level = copy.deepcopy(state[0])
            if card == 1:
                current_level[position] = 'X'

                if position - 1 >= 0:
                    previous_card = current_level[position - 1]
                    if previous_card == 0:
                        current_level[position - 1] = 1
                    elif previous_card == 1:
                        current_level[position - 1] = 0
                

                if position + 1 <= len(current_level) - 1:
                    previous_card = current_level[position + 1]
                    if previous_card == 0:
                        current_level[position + 1] = 1
                    elif previous_card == 1:
                        current_level[position + 1] = 0

                current_removed_cards = copy.deepcopy(state[1])
                current_removed_cards.append(position)

                current_state = copy.deepcopy(current_level)

                possible_states.append((current_state, current_removed_cards))

    return "No Solution!"


if __name__ == "__main__":
    main()