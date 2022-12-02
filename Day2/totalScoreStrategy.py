def calculateGameScore(strategy):
  opponentsMove,outCome = strategy.split(" ")

  victory = {'A': 'B', 'B': 'C', 'C': 'A'}
  loss = {'A': 'C', 'B': 'A', 'C': 'B'}

  points = {'A':1, 'B':2, 'C':3} 

  score = 0

  if outCome == 'Z':
    yourMove = victory[opponentsMove]
    score += 6
    score += points[yourMove]
  elif outCome == 'X':
    yourMove = loss[opponentsMove]
    score += points[yourMove]
  else:
    yourMove = opponentsMove
    score += 3
    score += points[yourMove]

  return score

strategyGuide = open('input.txt', 'r')
data = strategyGuide.readlines()

totalScore = 0
for game in data:
  baseData = game.split('\n')[0]
  gameScore = calculateGameScore(baseData)
  totalScore += gameScore

print(totalScore)