
from gameFunctions import winLose

def checkWhoWon(p, c):
  # tie
  if p == c:
    winLose.tie()

  # paper or scissors
  elif p == "paper":
    if (c == "scissors"):
      winLose.lose()
    else: 
      winLose.win()

  # scissors or rocks
  elif p == "scissors":
    if (c == "rock"):
      winLose.lose()
    else: 
      winLose.win()

  # rock and paper
  elif p == "rock":
    if (c == "paper"):
      winLose.lose()
    else: 
      winLose.win()
