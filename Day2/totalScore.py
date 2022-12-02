def calculateGameScore(strategy):
  opponentsMove,yourMove = strategy.split(" ")

  
  points = {'Y':2, 'X':1, 'Z':3} 
  convertedMoves = {'A': 'X', 'B': 'Y', 'C': 'Z'}

  score = points[yourMove]

  if yourMove == convertedMoves[opponentsMove]:
    score += 3
  elif (yourMove == 'Y' and convertedMoves[opponentsMove] == 'X') or (yourMove == 'X' and convertedMoves[opponentsMove] == 'Z') or (yourMove == 'Z' and convertedMoves[opponentsMove] == 'Y'):
    score += 6

  return score

strategyGuide = open('input.txt', 'r')
data = strategyGuide.readlines()

totalScore = 0
for game in data:
  baseData = game.split('\n')[0]
  gameScore = calculateGameScore(baseData)
  totalScore += gameScore

print(totalScore)