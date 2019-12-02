
import os

def getFuel(mass: int) -> int:
    return int(mass / 3 - 2)

def main():
    print(os.getcwd())
    inputFile = 'inputs/input01_2019.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part 1
    solution1 = sum([getFuel(int(l)) for l in lines])
    
    print('AoC 2019 - Day 01\n-----------------\nLength of Input (lines):\t{0}\n\nSolution:\nPart1:\t{1}\nPart2:\t{2}'.format(len(lines), solution1,0))
		
if __name__ == "__main__":
    main()
