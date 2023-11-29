def displayBoard():
    print("   " + game_play[0][0] + "   |   " + game_play[0][1] + "   |   "+ game_play[0][2] +"  ")
    print("______+______+______\n")
    print("   " + game_play[1][0] + "   |   " + game_play[1][1] + "   |   "+ game_play[1][2] +"  ")
    print("______+______+______\n")
    print("   " + game_play[2][0] + "   |   " + game_play[2][1] + "   |   "+ game_play[2][2] +"  ")
    print("\n")


def isoccupied(row, column):
    # verifie si la position n'a pas ete deja prise
    if(game_play[row - 1][column - 1] != ""):
        return True
    else: 
        return False
    
def user_input(player_number: int, input_type: str):
    # recuperation de la position du pion
    while True:
        if (value := int(input(f"Player {player_number} {input_type}: "))) <= 3:
            return value
        print("Out of range")
    
def check_victory(game_play, symbole):
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if all(game_play[i][j] == symbole for j in range(3)) or all(game_play[j][i] == symbole for j in range(3)) or all(game_play[i][i] == symbole for i in range(3))  or all(game_play[i][2 - i] == symbole for i in range(3)):
            return True
    return False

def exit_game():
    if(check_victory(game_play, "X")):
        return "X won"
        exit()
    elif(check_victory(game_play, "O")):
        return "O won"
        exit()
    else:
        return "It's a tie game"
    
def replay_game():
    if replay := input("Would you like to replay? (y/n): ").lower() == "y":
        return True
    else:
        print("Bye!")
        return False
        
def want_to_play():
        if replay := input("Would you like to play? (y/n): ").lower() == "y":
            return True
        else:
            return False
    
def init_game():
    global game_play
    game_play = [["" for _ in range(3)] for _ in range(3)]

    # debut du jeu
    displayBoard()
    print("All values should be between 1 and 3: ")
    for i in range(1,6): #range 6 parce que chaque joueur aura 4 tours plus le 1 tour pour le joueur X et ca fait 9 au total = nombre de place a occuper
        # 
        if(i == 5):
            while True:
                player_1_row, player_1_col = user_input(1, "row"), user_input(1, "column")
                
                if isoccupied(player_1_row, player_1_col):
                    print("Slot occupied")
                else:
                    game_play[player_1_row - 1][player_1_col - 1] = "X"
                    displayBoard()
                    break
        else: 
            while True:
                player_1_row, player_1_col = user_input(1, "row"), user_input(1, "column")
                
                if isoccupied(player_1_row, player_1_col):
                    print("Slot occupied")
                else:
                    game_play[player_1_row - 1][player_1_col - 1] = "X"
                    displayBoard()
                    break

            while True:
                player_2_row, player_2_col = user_input(2, "row"), user_input(2, "column")
                
                if isoccupied(player_2_row, player_2_col):
                    print("Slot occupied")
                else:
                    game_play[player_2_row - 1][player_2_col - 1] = "O"
                    displayBoard()
                    break
    print(exit_game())

if __name__ == "__main__":
    if(want_to_play()):
        init_game()
        while(replay_game()):
            init_game()
    