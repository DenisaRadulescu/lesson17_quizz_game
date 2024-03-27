# create a quizz game with admin and playes. A use has to login
# A user has to login, if player, the he can play, if adming, can add questions
import json
import time

import admin_functions
import users
import game






if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game!!"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    current_player = users.login()

    while True:
        if list(current_player.keys())[0] == 'admin':
            admin_functions.run()
        else:
            print(f"Let's play {list(current_player.keys())[0]}")
            game.run_game(current_player)
            user_pick = input("Do you want to play again? Y/N")
            if user_pick.lower() == "n":
                break

        time.sleep(2)
