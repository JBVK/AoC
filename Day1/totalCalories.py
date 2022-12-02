caloriesFile = open('input.txt', 'r')
data = caloriesFile.readlines()

mostCalories = 0
currentCalories = 0
for elf in data:
  baseData = elf.split('\n')[0]
  if baseData:
    currentCalories += int(elf)
  else:
    if currentCalories > mostCalories:
      mostCalories = currentCalories
      currentCalories = 0
    else:
      currentCalories = 0

print(mostCalories)