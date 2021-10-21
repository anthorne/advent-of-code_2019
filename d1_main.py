import sys
import math

totalFuelPartOne = 0
totalFuelPartTwo = 0
filerows = open('d1_input.txt')


def fuelcalc(mass):
    startfuel = math.trunc(float(mass.strip()) / 3) - 2
    fuelfuel = 0
    rest = startfuel
    while rest > 0:
        rest = math.trunc(float(rest) / 3) - 2
        if rest > 0:
            fuelfuel += rest
    return startfuel + fuelfuel


for mass in filerows:
    totalFuelPartOne += math.trunc(float(mass.strip()) / 3) - 2
    totalFuelPartTwo += fuelcalc(mass)

print(' Part One -- Total amount of energy needed: ' + str(totalFuelPartOne))
# 3278434

print(' Part Two -- Total amount of energy needed: ' + str(totalFuelPartTwo))
# 4914785

