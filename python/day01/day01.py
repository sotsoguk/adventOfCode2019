
import os

def getFuel(mass: int) -> int:
    if mass < 8:
        return 0
    return int(mass / 3 - 2)

def getRecFuel(mass: int) -> int:
   fuel = 0
   while mass >8:
       tmpFuel = getFuel(mass)
       fuel += tmpFuel
       mass = tmpFuel
   return fuel

def main():
    print(os.getcwd())
    inputFile = 'inputs/input01_2019.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part 1
    solution1 = sum([getFuel(int(l)) for l in lines])
    solution2 = sum([getRecFuel(int(l)) for l in lines])
    
    print('AoC 2019 - Day 01\n-----------------\nLength of Input (lines):\t{0}\n\nSolution:\nPart1:\t{1}\nPart2:\t{2}'.format(len(lines), solution1,solution2))
		
if __name__ == "__main__":
    main()
