import random

weights = [0 for i in range(15)]
bias = 7

digit0 = list('111101101101111')
digit1 = list('001001001001001')
digit2 = list('111001111100111')
digit3 = list('111001111001111')
digit4 = list('101101111001001')
digit5 = list('111100111001111')
digit6 = list('111100111101111')
digit7 = list('111001001001001')
digit8 = list('111101111101111')
digit9 = list('111101111001111')


digit50 = list('111000111001111')
digit51 = list('110100111001111')
digit52 = list('111100111001011')
digit53 = list('111100111001011')
digit54 = list('111100111011111')
digit55 = list('101100111001111')
digit56 = list('111100111001111')
digit57 = list('111100111001110')
digit58 = list('111100111001101')
digit59 = list('111100111000111')

digits = [digit0, digit1, digit2, digit3, digit4, digit5,
        digit6, digit7, digit8, digit9]

test_digits = [digit50, digit51, digit52, digit53, digit54,
        digit55, digit56, digit57, digit58, digit59]

def print_line(digits_array, line):
    output = ''
    for i in range(len(digits_array)):
        output += ' '
        for j in range(3):
            if digits_array[i][j + line * 3] == '0':
                output += ' '
            else:
                output += '#'
        output += '\t'
    print(output)

def print_digits(digits_array):
    lines_count = 5
    for i in range(lines_count):
        print_line(digits_array, i)

def print_digit(digit):
    for i in range(0, len(digit), 3):
        out = ''
        for j in range(3):
            if digit[i + j] == '1':
                out += '#'
            else:
                out += ' '
        print(out)

def increase(digit):
    for i in range(15):
        if int(digit[i]) == 1:
            weights[i] += 1

def decrease(digit):
    for i in range(15):
        if int(digit[i]) == 1:
            weights[i] -= 1

def proceed(digit):
    net = 0
    for i in range(15):
        net += int(digit[i]) * weights[i]
    return net >= bias

def train(times):
    for i in range(times):
        option = random.randint(0, 9)
        if option != 5:
            if proceed(digits[option]):
                decrease(digits[option])
        else:
            if not proceed(digit5):
                increase(digit5)

def print_results(digits):
    output_str = '\n'
    for i in range(len(digits)):
        output_str += ' '
        output_str += str(proceed(digits[i]))
        output_str += '\t'
    print(output_str, '\n')


def main():
    print("Weights before training: {}\n".format(weights))
    print("Answers before training(is five?): \n")
    print_digits(digits)
    print_results(digits)
    train(10000)
    print("Weights after training: {}\n".format(weights))
    print("Answers after training(is five?): \n")
    print_digits(test_digits)
    print_results(test_digits)

main()

