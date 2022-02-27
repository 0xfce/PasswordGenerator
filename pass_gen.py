from random import choice, shuffle
from argparse import ArgumentParser as ArgParser

parser = ArgParser()

parser.add_argument('-l', '--length', type=int, help='The lenght of the password.', default=16)
parser.add_argument('-s', '--symbols', action='store_true', help='Add symbols to the password.')
parser.add_argument('-u', '--uppercases', action='store_true', help='Add uppercases to the password.')
parser.add_argument('-n', '--numbers', action='store_true', help='Add numbers to the password.')

args = parser.parse_args()

symbols = [',', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', '/', '\\', '{', '}', '<', '>', '?', '_', '-', '+', '[', ']']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def generate() -> list:
    passwd = []
    for i in range(args.length):
        if args.symbols:
            passwd.append(choice(symbols))
        if args.numbers:
            passwd.append(choice(numbers))
        if args.uppercases:
            passwd.append(choice(alphabets))

        passwd.append(str(choice(alphabets)).lower())

    shuffle(passwd)

    return passwd[:args.length]


def format(lst: list) -> str:
    return str(lst).replace('[', '').replace('\'', '').replace(',', '').replace(']', '').replace(' ', '').replace('\"', '')

if __name__ == '__main__':
    print(format(generate()))
