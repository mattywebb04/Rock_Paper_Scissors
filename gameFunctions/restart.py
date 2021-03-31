from gameFunctions import config

# Win the entire game
def win():
  print(config.line)
  print('YOU WIN THE GAME!')
  print(config.line)
  replay()

# Lose the entire game
def lose():
  print(config.line)
  print("YOU LOSE THE GAME!")
  print(config.line)
  replay()


# Ask to replay
def replay():
  config.game_running = False
  answer = input("Play again? (y/n): ")

  if answer == "y":
    # Reset all values
    config.computer_lives = config.total_lives
    config.player_lives = config.total_lives
    config.game_running = True

  else:
    print('LEAVING PROGRAM!')
    exit()