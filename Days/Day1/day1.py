import sys

from usefulFunctions.usefulFunctions import getFileConts

# Pass the path to the data of choice and get the answer!

if __name__ == '__main__':
    pathToFile = sys.argv[1]
    fileContents = getFileConts(pathToFile)
    # Use double newline to determine the elves being split
    elves = []
    for elf in fileContents.split('\n\n'):
        sum = 0
        # We can then use the individual new lines to further split
        for item in elf.split('\n'):
            sum += int(item)
        elves.append(sum)
    print(f'Answer = {max(elves)}')
