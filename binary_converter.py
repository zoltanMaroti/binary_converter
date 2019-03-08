def binary_converter(number):
    number = str(number)
    power = len(number)-1
    values_list = []
    for i in number:
        index = int(i)
        value = index * 2 ** power
        values_list.append(value)
        power -= 1
    number = sum(values_list)
    return number


def decimal_converter(number):
    binary_list = []
    while number != 0:
        remainder = str(number % 2)
        number = number // 2
        binary_list.append(remainder)
    number = int("".join(binary_list[::-1]))
    return number


def print_binary_converter(number, parameter):
    if parameter == 2:
        print(binary_converter(number), "10")
    if parameter == 10:
        print(decimal_converter(number), "2")


def main():
    while True:
        try:
            number = input('Please enter a number to convert or "exit" to quit: ')
            if number == 'exit':
                exit()
            number = int(number)
            parameter = int(input("10 or 2 system? "))
            print_binary_converter(number, parameter)
        except ValueError:
            print("That's not a valid number!")


main()
