def getFileConts(pathToFile):
    file = open(pathToFile)
    fileContents = file.read()
    return fileContents