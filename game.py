import random #this module is used to get random numbers .
def roll_the_dice():
    minimum=1
    maximum=6
    roll_the_dice = random.randint(minimum,maximum)
    return roll_the_dice

while True:
    players = input("Enter how many players are playing. Enter between (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=4:
            break
        else:
            print("Enter the valid number between (2-4).")
    elif players.isalpha():
        # In this elif condition, if the user enter an alphabet,this condition will true.
        print("Invalid. Alphabet found. enter a digit between (2-4).")
    else:
        # In this else condition, if the user enter a punctuations or negative numbers, this condition will true.
        print("Invalid. Enter a digit between (2-4).")
final_score=50 # Assigned a value as my final score ( the player who reach this score first, then he will be the winner).
player_scores=[0 for i in range(players)] # This will be the first score of both players, first it will looks like [0,0,0,0].
while max(player_scores) < final_score:
    for i in range(players):
        print(f"\nplayer{i+1}, your chance is started.\n")
        print(f"Your total score is {player_scores[i]}")
        current_score = 0
        while True:
            rolling = input("Would you like to roll (y)? ")
            if rolling.lower() != "y":
                break
            value = roll_the_dice()
            if value == 1:
                print("You got 1, your current score is 0 and your chance is over wait for other players to finish their chances.")
                current_score=0
                break
            else:
                current_score += value
                print(f"You rolled and got {value}")
            print(f"Your score is {current_score}")
        player_scores[i]+=current_score
        total=f"total score is {player_scores[i]}"
        print(total)
maximum_score=max(player_scores)
player_winning_index=player_scores.index(maximum_score)
print(f"Player number {player_winning_index+1} is the winner and the score is {maximum_score}.")
