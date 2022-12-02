caloriesFile = open('input.txt', 'r')
data = caloriesFile.readlines()

elfsCalories = []
currentCalories = 0
for elf in data:
  baseData = elf.split('\n')[0]
  if baseData:
    currentCalories += int(elf)
  else:
    elfsCalories.append(currentCalories)
    currentCalories = 0

caloriesFile.close()

elfsCalories.sort()

top3Calories = 0
for calories in elfsCalories[-3:]:
  top3Calories += calories

print(top3Calories)
