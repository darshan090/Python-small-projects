import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symble_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symble_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnning_line.append(line + 1)
    return winnings, winnning_line

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
    print("-" * (len(columns) * 4 - 1))  # Add a separator line after each row

def deposit():
    while True:
        amount = input("Enter amount to deposite $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount should be greater than Zero")
        else:
            print("Enter a valid amount")

def get_number_of_lines():
    while True:
        lines = input("Enter a number of lines would you lie to place bet(1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a validnumber of line")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("Enter amount would you like to place bet$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"You do not bet more than your balance, your current balance is ${balance}")
        else:
            break 
    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symble_count)
    print_slot_machine(slots) 
    winnings,winning_lines = check_winnings(slots,lines,bet,symble_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance+=spin(balance)
    
    print(f"You left with ${balance}")
    
main()