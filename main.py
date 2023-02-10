import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COL = 3

symbol_count = {
    "7s": 2,
    "Bar": 4,
    "Cherries": 6,
    "Bells": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


# what values go in each column
# define columns list
    columns =[]
# generate a column for each number of columns
# picks random values for each row in column
    for _ in range(cols):
        column = []
# [:] creates a copy of the list-- so we dont select something twice
# current symbols is equal to A COPY of all symbols
        current_symbols = all_symbols[:]
# loop through number of values we need to generate (equal to the number of rows we have in slot machine)
        for _ in range (rows):
# first value we are picking is a Random Choice of all the symbols
            value = random.choice(all_symbols)
# remove the value so we dont pick it again
            current_symbols.remove(value)
# add value to column (up top)
            column.append(value)
# add column to our columns list
        columns.append(column)

    return columns

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if not lines.isdigit():
            print("Please enter a number.")
            continue
        lines = int(lines)
        if 1 <= lines <= MAX_LINES:
            break
        else:
            print("Enter a valid number of lines.")
            
    return lines

def get_bet():
    while True:
        bet = input("What would you like to wager on each line?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Enter a valid bet.")

    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}. Good luck.")


main()
