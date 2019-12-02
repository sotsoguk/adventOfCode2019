
import os
import itertools
from typing import List

def runCode(originalCode: List[int], noun,verb :int) -> int:
    code = originalCode.copy()
    code[1:3] = [noun,verb]
    ptr = 0
    while code[ptr] != 99:
        if code[ptr] == 1:
            code[code[ptr+3]] = code[code[ptr+1]] + code[code[ptr+2]]
        elif code[ptr] == 2:
            code[code[ptr+3]] = code[code[ptr+1]] * code[code[ptr+2]]
        else:
            break
        ptr += 4
    return code[0]

def main():
    print(os.getcwd())
    inputFile = 'inputs/input02_2019.txt'
    
    with open(inputFile) as f:
        lines = f.read().splitlines()
    
    code = [int(i) for i in lines[0].split(',')]
    
    # part 1
    solution1 = runCode(code,12,2)
    
    # part 2
    goal = 19690720
    
    n = range(100)
    v = range(100)
    for p in list(itertools.product(n,v)):
        if runCode(code,p[0], p[1]) == goal:
            solution2 = 100*p[0] + p[1]
            break
    print('AoC 2019 - Day 02\n-----------------\nLength of Input (lines):\t{0}\n\nSolution:\nPart1:\t{1}\nPart2:\t{2}'.format(len(lines), solution1,solution2))

if __name__ == "__main__":
    main()
