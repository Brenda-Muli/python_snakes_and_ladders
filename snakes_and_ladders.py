
import random
import time

# Variables for time, highest point which is 100 and sides of a dice
sleep_between_actions = 1
maximum_value = 100
dice_number = 6

# Snake positions: key = snake head, value = tail
snakes = {
    17: 6,
    54: 34,
    62: 19,
    64: 60,
    87: 36,
    93: 73,
    95: 75,
    98: 79
}

# Ladder positions: key = bottom, value = top
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}

# Text options for player's turn
player_turn_text = [
    'Your turn.',
    'Go.',
    'Ready?',
    'Proceed'
]

# Text options for snake bites
snake_bite = [
    'bummer',
    'oh no'
]

# Text options for ladder jumps
ladder_jump = [
    'yayy',
    'nailed it'
]

# Function to print the welcome message
def welcome_message():
    message = '''
    Welcome to Snakes and Ladders Game.
    Version 1.0.0
    Rules:
        1. Initially both players are at starting position.
            Take it in turns to roll the dice.
            Move forward the number of spaces shown on the dice.
        2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
        3. If you land on the head of a snake, you must slide down to the bottom of the snake.
        4. The first player to get to the FINAL position is the winner.
        5. Hit enter to roll the dice.
    '''
    print(message)


# Function to get players' names
def get_player_name():
    player_one = None
    while not player_one:
        player_one = input('Please enter first player name: ').strip()

    player_two = None
    while not player_two:
        player_two = input('Please enter second player name: ').strip()

    print(f'Match will be played between {player_one} and {player_two}')
    return player_one, player_two


# Function to roll the dice and get a random value
def get_dice_value():
    time.sleep(sleep_between_actions)
    dice_value = random.randint(1, dice_number)
    print(f'It is a {dice_value}')
    return dice_value


# Function to handle the event of a snake bite
def got_snake_bite(old_value, current_value, player_name):
    print(random.choice(snake_bite).upper())
    print(f'{player_name} got bitten and goes down from {old_value} to {current_value}')


# Function to handle the event of a ladder jump
def got_ladder_jump(old_value, current_value, player_name):
    print(random.choice(ladder_jump).upper())
    print(f'{player_name} climbed up the ladder from {old_value} to {current_value}')


# Function to update the player's position considering snakes and ladders
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(sleep_between_actions)
    old_value = current_value
    current_value += dice_value

# Check if player has moved past the winning position
    if current_value > maximum_value:
        print(f'You need {maximum_value - old_value} to win. Keep trying')
        return old_value
    print(f'{player_name} moved from {old_value} to {current_value}')

# Handle snake bite if player lands on a snake head
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

# Handle ladder jump if player lands at the bottom of a ladder
    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value

    return final_value


# Function to check if a player has won the game
def check_win(player_name, position):
    if position == maximum_value:
        print(f'''
        Game Over!
        {player_name} has won the game
        Congratulations {player_name} you win this round!
        ''')
        return True
    return False


# Main function to start and manage the game
def start():
    welcome_message()
    time.sleep(sleep_between_actions)
    player_one, player_two = get_player_name()
    time.sleep(sleep_between_actions)

    player_one_current_position = 0
    player_two_current_position = 0

    while True:
        time.sleep(sleep_between_actions)
        input(f'{player_one} : {random.choice(player_turn_text)} Hit enter to roll dice: ')
        print('Rolling dice...')
        dice_value = get_dice_value()  # Roll the dice for player one
        time.sleep(sleep_between_actions)
        print(f'{player_one} moving...')
        player_one_current_position = snake_ladder(player_one, player_one_current_position, dice_value)

        if check_win(player_one, player_one_current_position):
            break

        time.sleep(sleep_between_actions)
        input(f'{player_two} : {random.choice(player_turn_text)} Hit enter to roll dice: ')
        print('Rolling dice...')
        dice_value = get_dice_value()
        time.sleep(sleep_between_actions)
        print(f'{player_two} moving...')
        player_two_current_position = snake_ladder(player_two, player_two_current_position, dice_value)

        if check_win(player_two, player_two_current_position):
            break


# Run the game if this script is executed directly
if __name__ == '__main__':
    start()