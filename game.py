from random import randint

from gameFunctions import config, winLose, compare, restart

# possible choices for the user
choices = ["rock", "paper", "scissors"]

while config.game_running is True:

  player = input("Please type rock, paper, or scissors: ")

  # Check if user wants to exit
  if player == 'exit':
    print('Exiting Program!')
    exit()

  computer = choices[randint(0,2)]

  # Compare the results
  compare.checkWhoWon(player, computer)
  
  # Checks if game is over
  if config.player_lives <= 0:
    restart.lose()
  elif config.computer_lives <= 0:
    restart.win()
  
  print('Player: ', config.player_lives, '/', config.total_lives)
  print('Computer: ', config.computer_lives, '/', config.total_lives,'\n')