def main():
    
    a = [1, 2, 3]
    print(f"Original list: {a}")
    print(f"Reversed list: {ReverseList_Slicing(a)}")

    return 0


def ReverseList_Slicing(list):
    reversed_list = list[::-1]

    return reversed_list


if __name__ == "__main__":
    main()