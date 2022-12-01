import sys

from usefulFunctions.usefulFunctions import getFileConts

# Pass the path to the data of choice and get the answer!

if __name__ == '__main__':
    pathToFile = sys.argv[1]
    fileContents = getFileConts(pathToFile)
    # Use double newline to determine the elves being split
    elves = []
    for elf in fileContents.split('\n\n'):
        thisSum = 0
        # We can then use the individual new lines to further split
        for item in elf.split('\n'):
            thisSum += int(item)
        elves.append(thisSum)
    elves.sort(reverse=True)
    print(f'Answer to part 1 = {elves[0]}')
    print(f'Answer to part 2 = {sum(elves[0:3])}')
