from gameFunctions import config


def win():
  print(config.line)
  print('You win this round!')
  print(config.line, '\n')
  config.computer_lives = config.computer_lives - 1

def lose():
  print(config.line)
  print('You lose this round!')
  print(config.line, '\n')
  config.player_lives = config.player_lives - 1

def tie():
  print(config.line)
  print('Round was a tie')
  print(config.line, '\n')



