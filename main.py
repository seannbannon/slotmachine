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
