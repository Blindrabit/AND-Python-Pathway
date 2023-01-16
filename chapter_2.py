import random


class Employee:
    def __init_(self, first_name: str, second_name: str):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self) -> str:
        """
        full_name returns the {first_name} {second_name}
        """
        return self.full_name

    @property
    def email(self) -> str:
        """
        email returns {first_name}.{second_name}@and.digital.co.uk
        """
        return f"{self.first_name.lower()}.{self.second_name.lower}@and.digital.co.uk"


def rock_paper_scissors() -> tuple[int, int]:
    options = ["rock", "paper", "scissors"]
    player_choice = input("choose rock, paper or scissors? ").lower()
    if player_choice not in options:
        print("incorrect choice! please choose rock, paper or scissors")
        return rock_paper_scissors()
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        print("It's a draw")
    elif player_choice == options[0] and computer_choice == options[2]:
        print("You Win")
        return 1, 0
    elif player_choice == options[1] and computer_choice == options[0]:
        print("You Win")
        return 1, 0
    elif player_choice == options[2] and computer_choice == options[1]:
        print("You Win")
        return 1, 0
    else:
        print("You Lose")
        return 0, 1


def rock_paper_scissors_games(players_score: int = 0, computer_score: int = 0):
    number_of_rounds = input("How many rounds would you like to play as an integer? ")
    try:
        number_of_rounds = int(number_of_rounds)
    except ValueError:
        print("please choose an integer.")
        return rock_paper_scissors_games(players_score, computer_score)
    for n in range(int(number_of_rounds)):
        player, computer = rock_paper_scissors()
        players_score += player
        computer_score += computer
        print(f"the current score is {players_score} - {computer_score}")
    while True:
        play_more = input("would you like to play more rounds, choose yes or no ")
        if play_more not in ["yes", "no"]:
            print("please choose yes or no! ")
        elif play_more.lower() == "no":
            print(f"Thanks for playing! The final score was {players_score} - {computer_score}")
            return False
        else:
            return rock_paper_scissors_games(players_score, computer_score)


if __name__ == '__main__':
    rock_paper_scissors_games()
