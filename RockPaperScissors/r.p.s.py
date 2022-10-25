import random

while True:

    def play():
        user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors:")
        computer = random.choice(['r', 'p','s'])

        if user == computer:
            return "It's a tie"

        if is_win(user, computer):
            return  "You won!"



        return "You lost!"

    def is_win(player, oppnent):
        if (player == "r" and oppnent == "s") or (player == "s" and oppnent == "p") or (player == "p" and oppnent == "r"):
            return True

    print(play())