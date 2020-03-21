letter_val = {" ": 0, "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2,
              "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
              "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
              }
print("""

       _/_/_/_/    _/_/_/_/   _/_/_/_/     _/       _/_/_/_/    _/_/_/_/    _/        _/_/_/_/
      _/         _/         _/     _/    _/ _/     _/     _/   _/     _/   _/        _/
     _/_/_/_/   _/         _/_/_/_/    _/   _/    _/_/_/_/    _/_/_/_/    _/        _/_/_/_/
           _/  _/         _/ _/       _/_/_/_/   _/     _/   _/     _/   _/        _/
    _/_/_/_/  _/_/_/_/   _/    _/    _/     _/  _/_/_/_/    _/_/_/_/    _/_/_/_/  _/_/_/_/
""")
players = []

# Adds Players
def add_players():
    print("If amount of players is less than 4, press enter after all players are entered.")
    while len(players) < 4:
        new_player = input("Enter player to add>>> ")

        if new_player:
            if new_player not in (stats[0] for stats in players):
                players.append([new_player, 0])
                print(f"Player {new_player} added.")
            else:
                print("Player already in player list.")
        else:
            break

# Function for starting program
def begin():
    add_players()
    main()

# Main menu where all actions are
def home():
    option = input('Would you like to [A]dd a score, [V]iew scores, [U]ndo the last change, or [End] the game? > ')
    return option

# Function for adding score of a word to a player
def add_score():
    # Declare globals
    global temp_value, temp_player, undo_ind
    player = input("Enter player to score>>> ")
    if player:
        if player in (stats[0] for stats in players):
            temp_player = player
            try:
                word = input("Enter word to score(Enter a space for blank tiles)>>> ")
                if word:
                    value = temp_value = sum(letter_val[i.upper()] for i in word)
                else:
                    add_score()
                    return
            except KeyError:
                print("Word must consist of letters only.")
                add_score()
                return
            # Multiplies letters by given multiplier
            print("Enter doubled or tripled letter as following> if a is doubled and b is tripled,"
                  " code is entered like this> a2 b3")
            mult_letters = input("Enter multiplied letters in the above format> ")
            spl_mult_letters = mult_letters.split()
            # Multiplies letters
            try:
                for letter, mult in spl_mult_letters:
                    if letter in word:
                        value = temp_value = value + letter_val[letter.upper()]*(int(mult)-1)
            except ValueError:
                print("Please enter multiplied letters in the shown format.")
                add_score()
            print("Is word doubled or tripled?")
            multiplier = input("Enter 2 for double and 3 for triple> ")
            try:
                value = temp_value = value * int(multiplier)
            except ValueError:
                print("Input was invalid.")
                add_players()
            # Adds score to player score
            for stats in players:
                if stats[0] == player:
                    stats[1] += value
        else:
            print("Player entered is not in player list.")
            add_score()
            return
    undo_ind = False
    main()

# Views scores of all players
def view_scores():
    for stats in players:
        print(f"Player {stats[0]} has a score of {stats[1]}")
    main()

# Undoes last score added
def undo():
    global undo_ind
    no_change = "No changes have been made."
    try:
        if temp_value and temp_player and not undo_ind:
            for stats in players:
                if stats[0] == temp_player:
                    stats[1] -= temp_value
        else:
            print(no_change)
    except NameError:
        print(no_change)
        main()
        return
    undo_ind = True
    main()
    return

# Prints score and ends game
def end_game():
    for name, score in players:
        print(f"Player {name} has a score of {score}")

# Main function
def main():
    option = home()
    while True:
        if option.lower() == "a":
            add_score()
        elif option.lower() == "v":
            view_scores()
        elif option.lower() == "u":
            undo()
        elif option.lower() == "end":
            end_game()
            exit()
        else:
            print("Please enter a valid option.")
            main()


if __name__ == "__main__":
    begin()
