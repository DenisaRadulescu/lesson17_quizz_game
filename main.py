# create a quizz game with admin and playes. A use has to login
# A user has to login, if player, the he can play, if adming, can add questions
import json
import users






if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game!!"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    users.login()